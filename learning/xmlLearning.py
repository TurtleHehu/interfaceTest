from xml.etree import ElementTree as ElementTree
import os
import readConfig

xml_path = os.path.join (readConfig.pro_Dir, 'testFile', 'SQL.xml')
with open (xml_path, encoding='UTF-8') as fp:
    et = ElementTree.parse (fp)
database = {}


class XmlLearning ():
    # for db in et.findall ("database"):
    #     db_name = db.get ("name")
    #     print (db_name)
    #     table = {}
    #     for tb in db.getchildren ():
    #         table_name = tb.get ("name")
    #         print (table_name)
    #         sql = {}
    #         for data in tb.getchildren ():
    #             sql_id = data.get ("id")
    #             print (sql_id)
    #             sql[sql_id] = data.text
    #             print (data.text)
    #         table[table_name] = sql
    #     database[db_name] = table

    def get_url_from_xml(self,name):

        """
        By name get url from interfaceURL.xml
        :param name: interface's url name
        :return: url
        """
        url_list = []
        url_path = os.path.join (readConfig.pro_Dir, 'testFile', 'interfaceURL.xml')
        tree = ElementTree.parse(url_path)
        for u in tree.findall('url'):
            url_name = u.get('name')
            if url_name == name:
                for c in u.getchildren():
                    url_list.append(c.text)

        url = '/' + '/'.join(url_list)

        return url


if __name__ == "__main__":
    xl = XmlLearning()
    url = xl.get_url_from_xml('login')
    print(url)