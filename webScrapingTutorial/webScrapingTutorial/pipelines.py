# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3

class WebscrapingtutorialPipeline:
    def __init__(self):
        self.database = "mydatabase1.db"
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect(self.database)
        self.curr = self.conn.cursor()

    def create_table(self):
        statement = f"""
         create table wine_table(
             winename text,
             volume text,
             price text,
             category text
         )
         """
        try:
            self.curr.execute(statement)
            self.conn.commit()
        except:
            pass

    def process_item(self, item, spider):
        statement = f"""
            insert into wine_table values(?,?,?,?)
            """
        self.curr.execute("""insert into wine_table values (?,?,?,?)""", (
            item['pName'],
            item['pVol'],
            item['pPrice'],
            item['pCategory']))

        self.conn.commit()
        return item


class JumiaPipeline:
    def __init__(self):
        self.database = "jumia.db"
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect(self.database)
        self.curr = self.conn.cursor()

    def create_table(self):
        statement = f"""
         create table phone_table(
             phoneName text,
             price text,
             description text
             
         )
         """
        try:
            self.curr.execute(statement)
            self.conn.commit()
        except:
            pass

    def process_item(self, item, spider):
        statement = f"""
            insert into phone_table values(?,?,?,?)
            """
        self.curr.execute("""insert into phone_table values (?,?,?)""", (
            item['phoneName'],
            item['price'],
            item['description']
            ))

        self.conn.commit()
        return item


class DictionaryExtractorPipeline():
    def __init__(self):
        self.database = "dictionary.db"
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect(self.database)
        self.cur = self.conn.cursor()

    def create_table(self):
        try:
            self.cur.execute("""
            create table definition_table(
                word text,
                pronunciation text,
                part_of_speech text,
                definitions text
            )
            """)
            self.conn.commit()
        except:
            pass

    def process_item(self, item, scrapy):
        self.cur.execute("""insert into definition_table values(?,?,?,?)""", (
                         item['word'],
                         item['pronunciation'],
                         item['partOfSpeech'],
                         item['definitions']
                         ))
        self.conn.commit()
        return item


