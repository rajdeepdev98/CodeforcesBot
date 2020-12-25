import os
import requests
from bs4 import BeautifulSoup

def probparser(page_url):
    #This function returns the problem tags from the problems page
    response=requests.get(page_url)
    if(not response.ok):
        print("Problem page not found...")
    soup=BeautifulSoup(response.text,'lxml')
    problemsec=soup.find('table',class_='problems')
    if(not problemsec):
        print("Couldn't find problem section")
        return None
    problemtags=problemsec.find_all('a')
    # for el in problemtags:
    #     print(el.prettify())
    problems=[]
    length=len(problemtags)
    # print(length)
    for i in range(0,length,4):
        temp=problemtags[i].text
        problems.append(temp.strip())
    return problems

def test_case_parser(problem_url):
    #This function fetches testcases from the problem page using problem url
    response=requests.get(problem_url)
    if(not response.ok):
        print("Test cases couldn't be fetched...")
        return None,None
    probpage=response.text
    soup=BeautifulSoup(probpage,'lxml')
    input_sec=soup.find_all('div',class_='input')
    output_sec=soup.find_all('div',class_='output')
    inputs=[]
    outputs=[]
    length=len(input_sec)
    for i in range(length):
        tempin=input_sec[i].pre.text
        tempout=output_sec[i].pre.text
        inputs.append(tempin.strip())
        outputs.append(tempout.strip())
    return inputs,outputs

def main():
    print("Welcome Rajdeep! ")
    
    round_no=input("Round No : ")
    contest_id=input("ContestID : ")
    try:
        os.mkdir(round_no)
    except:
        print("Directory already exists")
    contest_url="https://codeforces.com/contest/"+contest_id
    #parsing the problem page
    print("Parsing the problem page.....")
    problems=probparser(contest_url)
    pno=len(problems)
    print(f'No of problems={pno}')
    print("Parsing problems....")
    for problem in problems:
        try:
            problem_url=contest_url+"/problem/"+problem
            inputs,outputs=test_case_parser(problem_url)
            probdr=round_no+"\\"+problem
            try:
                os.mkdir(probdr)
                path=probdr+"\\"+"sol.cpp"
                #cmmmnd stands for command
                cmmnd="copy mytemp.cpp "+path
                path2=probdr+"\\rn.bat"
                os.system(cmmnd)
                cmmnd2="copy runfile.bat "+path2
                os.system(cmmnd2)
            except:
                print("Problem Directory already exists!!...")
            length=len(inputs)
            for i in range(length):
                infile="in"+str(i+1)+".txt"
                outfile="out"+str(i+1)+".txt"
                inpath=round_no+"/"+problem+"/"+infile
                outpath=round_no+"/"+problem+"/"+outfile
                with open(inpath,'w') as file:
                    file.write(inputs[i])
                with open(outpath,'w') as file:
                    file.write(outputs[i])
        except:
            print ("Error in parsing test cases....")
            return
    print("Problems parsed and test cases downloaded.....")


if __name__ == "__main__":
    main()
     
   
                





