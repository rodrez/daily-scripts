from sys import stdout
from time import sleep
import pandas as pd
import requests
from bs4 import BeautifulSoup


# career_build = 'https://www.careerbuilder.com'


# Global Variables
job = 'junior software engineer'  # input("Enter your future job: \n")
location = 'Mechanicsburg, PA'  # input("Enter the desired location: \n")


def j_containers(job, location):
    current_url = f"https://www.careerbuilder.com/jobs?utf8=%E2%9C%93&keywords=" \
                  f"{job.replace(' ', '+')}&location={location.replace(' ', '+')}"
    web = requests.get(current_url).text
    soup = BeautifulSoup(web, 'html.parser')
    job_containers = soup.select('.data-results-content-parent')

    return job_containers

def sign_in_removal(job_containers_list):
    """
    Removes the sign in link to avoid signing in to the CB page.
    Grabs the link for each job container and saves it to saved_jobs
    :param job_containers_list: list using the select function from bs4
    :return: saved_jobs list
    """
    # Career Builder sign in url
    sign_in_url = "https://www.careerbuilder.com/user/sign-in?next="
    saved_jobs = []
    for idx, jobs in enumerate(job_containers_list):
        saved_jobs.append(f'{job_containers_list[idx].a.get("href", None).replace(sign_in_url, "")}')
    return saved_jobs


def job_information(url):
    website = requests.get(url).text
    job_soup = BeautifulSoup(website, 'html.parser')

    # application_type = 'regular'
    job_name = job_soup.select('.dib-m > h1')[0].getText()



    company_name = job_soup.select('.data-details > span:nth-child(1)')[0].getText()
    job_location = job_soup.select('.data-details > span:nth-child(2)')[0].getText()
    # apply_url = job_soup.select('.external-apply-link')[0].get('href', None)
    # company_url = soup.select(".icl-u-lg-mr--sm > a")[0].get("href", None)

    job_data = {'Job Title': job_name, 'Company': company_name, 'Location': job_location, 'Application Url': url}

    return job_data


def add_to_csv(job_dict, idx_counter):
    """
    Uses pandas to convert a dictionary to a csv file.
    :param idx_counter: integer Normally used as the for loop counter tor assign index
    :param job_dict: Dictionary
    """
    df = pd.DataFrame([job_dict], index=[idx_counter])
    df.to_csv('panda_job_data.csv', mode='a+', header=False)


def run_data_collection(job, location):
    """
    Runs the code and and shows the progress of the dat collection
    :param job: Takes a string with the job title
    :param location: Takes a string with the job location
    """
    counter = 0

    for jobs in sign_in_removal(j_containers(job, location)):
        counter += 1
        sleep(.1)
        stdout.write('\rCollecting information. Jobs collected %s' % counter)
        stdout.flush()
        add_to_csv(job_information(jobs), counter)
    print(f'\n{counter} jobs were added to the csv file.' )


run_data_collection(job, location)
