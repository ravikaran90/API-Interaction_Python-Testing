#!/usr/bin/python3

import datetime
from api_interaction import WebsiteInteraction


class Testing():

    #Testing title_post99 method from api_interaction.py against this fixed string
    def test_title(self):
        ob1=WebsiteInteraction()
        assert ob1.title_post99() =='temporibus sit alias delectus eligendi possimus magni'

    #Testing insert_time method against a combination of a fixed output from post 100 and present time
    def test_time(self):
        ob2=WebsiteInteraction()
        utc_time=datetime.datetime.now(datetime.timezone.utc)
        new_format=utc_time.strftime("%d/%m/%Y %H:%M:%S")
        record={'userId': 10, 'id': 100,
                'title': 'at nam consequatur ea labore ea harum',
                'body': 'cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qu' \
                                        'i minus magnam et distinctio eum\naccusamus ratione error aut', 'time':''}
        record['time']=new_format
        assert ob2.insert_time()==record

    #Testing new_post_and_checking method from api_interaction.py against a tuple having fixed values
    def test_post(self):
        ob3=WebsiteInteraction()
        assert ob3.new_post_and_checking()==(101, 201, 'Express')

    #Testing printing_tuple method's output from api_interaction.py against a fixed tuple
    def test_printing_tuple(self):
        ob4=WebsiteInteraction()
        assert ob4.printing_tuple((ob4.new_post_and_checking()))==(101, 201, 'Express')

    #Testing deleting_record method with a successful return status code and value of x-content-type-options
    def test_deleting_record(self):
        ob5=WebsiteInteraction()
        assert ob5.deleting_record((ob5.new_post_and_checking()))==(200,'nosniff')


def main():
    #Creating an object of Testing class
    test_obj=Testing()

    #Calling test_title method
    test_obj.test_title()

    #Calling test_time method
    test_obj.test_time()

    #Calling test_post method
    test_obj.test_post()

    #Calling test_printing_tuple method
    test_obj.test_printing_tuple()

    #Calling test_deleting_record method
    test_obj.test_deleting_record()


if __name__=='__main__':
    main()
