"""
1.Create a function which takes in 3 arguments: job_title, start_date, finish_date
2.Create a list with these 3 arguments in order and call the function by UNPACKING the list into it as arguments
3.Create a dictionary with these 3 arguments in and call the function by UNPACKING the dictionary into it as arguments
4.Create a decorator called with_job_title which always passes in some fixed job title to the function above
5.Wrap the function in using the decorator and call it, passing in the arguments excluding job_title
"""

def task(job_title, start_date, finish_date):
    print(job_title)
    print(start_date)
    print(finish_date)
    pass

list_with_arguments = ('Interpreter', '12.09.2021', '16.09.2021')
task(*list_with_arguments)

dict_of_arguments = {
    'job_title' : 'Interpreter',
    'start_date' : '12.09.2021',
    'finish_date' : '16.09.2021'

}

task(**dict_of_arguments)

def with_job_title(task):
    def wrapper():
        task(job_title='Carpenter')
