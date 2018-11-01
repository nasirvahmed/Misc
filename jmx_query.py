#!/usr/bin/python
import sys
import json
import time
import subprocess
from datetime import date

JMX_JAR = '/opt/telegraf/JMXQuery-0.1.8.jar'
HOST = 'localhost'
USER = 'admin'
PASS = 'admin123'

def heap_memory():
    output = subprocess.Popen(['java', '-jar', JMX_JAR, '-u', USER, '-p', PASS, '-url', 'service:jmx:rmi:///jndi/rmi://' + HOST + ':1099/jmxrmi', '-q', 'java.lang:type=Memory/HeapMemoryUsage/used', '-json'], stdout=subprocess.PIPE).communicate()[0]
    json_out = json.loads(output)
    for i in range(len(json_out)):
        if json_out[i]['value']:
            print json_out[i]['attribute'], json_out[i]['attributeKey'] + '=' + str(json_out[i]['value'])
    
    
def non_heap_memory():
    output = subprocess.Popen(['java', '-jar', JMX_JAR, '-u', USER, '-p', PASS, '-url', 'service:jmx:rmi:///jndi/rmi://' + HOST + ':1099/jmxrmi', '-q', 'java.lang:type=Memory/NonHeapMemoryUsage/used', '-json'], stdout=subprocess.PIPE).communicate()[0]
    json_out = json.loads(output)
    for i in range(len(json_out)):
        if json_out[i]['value']:
            print json_out[i]['attribute'], json_out[i]['attributeKey'] + '=' + str(json_out[i]['value'])

def gc():
    output = subprocess.Popen(['java', '-jar', JMX_JAR, '-u', USER, '-p', PASS, '-url', 'service:jmx:rmi:///jndi/rmi://' + HOST + ':1099/jmxrmi', '-q', 'java.lang:type=GarbageCollector,name=PS MarkSweep/CollectionCount', '-json'], stdout=subprocess.PIPE).communicate()[0]
    json_out = json.loads(output)
    for i in range(len(json_out)):
        print 'GC', json_out[i]['attribute'] + '=' + str(json_out[i]['value'])

def db_conn():

    output = subprocess.Popen(['java', '-jar', JMX_JAR, '-u', USER, '-p', PASS, '-url', 'service:jmx:rmi:///jndi/rmi://' + HOST + ':1099/jmxrmi', '-q', 'org.mongodb.driver:type=ConnectionPool,clusterId=*,host=*,port=*/Size', '-json'], stdout=subprocess.PIPE).communicate()[0]
    json_out = json.loads(output)
    for i in range(len(json_out)):
        print 'DB,db_name=' + json_out[i]['mBeanName'].split(',')[2][5:],json_out[i]['attribute'] + '=' + str(json_out[i]['value'])

def tc():
    output = subprocess.Popen(['java', '-jar', JMX_JAR, '-u', USER, '-p', PASS, '-url', 'service:jmx:rmi:///jndi/rmi://' + HOST + ':1099/jmxrmi', '-q', 'java.lang:type=Threading/ThreadCount', '-json'], stdout=subprocess.PIPE).communicate()[0]
    output2 = subprocess.Popen(['java', '-jar', JMX_JAR, '-u', USER, '-p', PASS, '-url', 'service:jmx:rmi:///jndi/rmi://' + HOST + ':1099/jmxrmi', '-q', 'java.lang:type=Threading/PeakThreadCount', '-json'], stdout=subprocess.PIPE).communicate()[0]
    json_out = json.loads(output)
    for i in range(len(json_out)):
        if json_out[i]['value']:
            print 'Threads', json_out[i]['attribute'] + '=' + str(json_out[i]['value'])
    
    json_out = json.loads(output2)
    for i in range(len(json_out)):
        if json_out[i]['value']:
            print 'Threads', json_out[i]['attribute'] + '=' + str(json_out[i]['value'])

if __name__ == "__main__":
    # Heap Memory
    heap_memory()
    # Non Heap Memory
    non_heap_memory()
    # Garbage Collection
    gc()
    # Thread Count
    tc()
    # DB Connections
    db_conn()
