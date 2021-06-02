#!/usr/bin/python3

import urllib.request
import requests
import json
import datetime


class WebsiteInteraction():

    url="http://jsonplaceholder.typicode.com/posts/"
    try:
        response=urllib.request.urlopen(url)
        listing=json.loads(response.read())
    except urllib.request.HTTPError as exception:
        print(exception)

    #Method to get the Title for Post Number 99
    def title_post99(self):
        for i in self.listing:
            if i['id']==99:
                print("Title of the post 99:",i['title'])
                return i['title']
            else:
                continue
        return 'Post with id 99 not present'

    #Method for Inserting Time(UTC)
    def insert_time(self):
        utc_timing=datetime.datetime.now(datetime.timezone.utc)
        time_to_insert=utc_timing.strftime("%d/%m/%Y %H:%M:%S")
        for t in self.listing:
            if t['id']==100:
                t['time']=time_to_insert
                print('100th Record after inserting current time(UTC):',t)
                return t
            else:
                continue
        return 'Post with id 100 not present'

    #Method for new entry in /posts
    def new_post_and_checking(self):
        new_post={}
        new_post['Title']="Security Interview Post"
        new_post['UserID']=500
        new_post['Body']="This is an insertion test with known API"
        resp=requests.post(self.url,data=new_post)
        if resp.status_code>=200 and resp.status_code<=299:
            return (resp.json()['id'],resp.status_code,resp.headers['X-Powered-By'])
        else:
            return 'New posting was not successful'

    #Method for printing the newly created tuple
    def printing_tuple(self,new_tuple):
        print(new_tuple)

        return new_tuple

    #Method for deleting the record through "id"
    def deleting_record(self,new_tuple):
        if type(new_tuple) is tuple:
            try:
                delete_url=self.url+str(new_tuple[0])
                delete_resp=requests.delete(delete_url)
            except IndexError as exception:
                print(exception)
            except:
                print("Deletion didn't happen")
            else:
                print('Status Code:',delete_resp.status_code)
                print('x-content-type-options:',delete_resp.headers['x-content-type-options'])
                return delete_resp.status_code,delete_resp.headers['x-content-type-options']
        else:
            return 1

def main():
    #Creating an object of Class WebsiteInteraction
    obj=WebsiteInteraction()

    #Calling the method to get the title for post 99
    obj.title_post99()

    #Calling Insert time method
    obj.insert_time()

    #Creating a new post, checking if the post was successful and creating a tuple
    new_tup=obj.new_post_and_checking()

    #Calling the method to print the new tuple
    obj.printing_tuple(new_tup)

    #Calling the method to delete the record through new 'id'
    obj.deleting_record(new_tup)

if __name__=='__main__':
    main()
