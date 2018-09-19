#!usr/bin/env python
# -*- coding: utf-8 -*-
'''Week 2 - Assignment 1'''

import urllib2
import csv
import datetime
import logging
import argparse
import sys

#url = 'https://s3.amazonaws.com/cuny-is211-spring2015/birthdays100.csv'

def main():
    '''Takes a CSV file and stores the data as a dictionary.'''

    def downloadData(url):
        '''Downloads CSV file from the url.'''
        if url is None:
            sys.exit()
        else:
            urlData = urllib2.urlopen(url)
            return urlData

    def processData(data):
        '''Process data from the csv file downloaded from a url.'''
        csv_file = csv.reader(data)
        person_dictionary = {}
        csv_file.next()

        for row in csv_file:
            try:
                row[2] = datetime.datetime.strptime(row[2], '%d/%m/%Y')
            except ValueError:
                idnumber = int(row[0])
                line = int(row[0])+1
                logger = logging.getLogger('assignment2')
                logger.error('Error processing line #' + line +'for ID #' + idnumber)

            person_dictionary[int(row[0])] = (row[1], row[2])
        return person_dictctionary

    def displayPerson(id, personData):
        '''takes in an integer called i​ds and stors it as a dictionary.'''
        try:
            response = 'Person #{idnum} is {name} with a birthday of {date}'
            print response.format(idnum=id, name=personData[id][0], date=personData[id][1])
        except KeyError:
            print 'No person found try another ID number.'

    parser = argparse.ArgumentParser()
    parser.add_argument('--url')
    args = parser.parse_args()
    logging.basicConfig(filename='errors.log', level=logging.ERROR)

    if args.url:
        csvData = downloadData(args.url)
        personData = processData(csvData)
        msg = 'Please enter an ID number.  Enter 0 or a negative number to exit. '

        while True:
            try:
                user = int(raw_input(msg))
            except ValueError:
                print 'Your input is not a valid id number. Please try again.'
                continue
            if user > 0:
                displayPerson(user, personData)
            else:
                pass

if __name__ == '__main__':
    main()
