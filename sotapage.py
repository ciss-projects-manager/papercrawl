import requests
from lxml import etree

class sotaPage(object):
    def __init__(self):
        self.sota_url = 'https://www.paperswithcode.com/sota'
        self.containerdict = {}

    def request_sotapage(self):
        taskdict = {}
        response = requests.get(url=self.sota_url)
        html = etree.HTML(response.text)
        content = html.xpath("/html/body/div[@class='container']//div[@class='infinite-container featured-task']")[0]
        grouptitles = content.xpath("./div[@class='row task-group-title']/div[@class='col-md-12']/h4/a/text()")
        alltasks = content.xpath("./div[@class='sota-all-tasks']/a/@href")
        tasks = content.xpath("./div[@class='sota-all-tasks']/a/text()")
        taskcounts = ["".join(list(filter(str.isdigit,task))) for task in tasks]
        for grouptitle,alltask,taskcount in zip(grouptitles,alltasks,taskcounts):
            task_value = alltask,taskcount
            taskdict[grouptitle] = task_value
        return taskdict



if __name__ == '__main__':
    obj = sotaPage()
    print(obj.request_sotapage())
