"""
https://zenn.dev/myuki/books/02fe236c7bc377/viewer/16fd5a
"""

import sys
import os
import re
import json
import codecs
# from sqlalchemy import Column, String
# from sqlalchemy.orm import declarative_base


# url = 'mysql+mysqldb://root@localhost/test?charset=utf8'
# engine = create_engine(url, echo=True)
# Base = declarative_base()

# class hash(Base):
#     __tablename__ = 'hashs'
#     func = Column(String, primary_key=True)
#     group = Column(String)
#     group_index = Column(String)
#     bit_index = Column(String)
#     deptcode = Column(String)

def main():
    file_data = codecs.open("C:\\Users\\eggow\\OneDrive\\ドキュメント\\Github\\gen_hash_table\\table.txt", "r", "utf-8_sig" , "ignore")#ファイル読み込み
    out_file = open("out.txt",'a')
    for line in file_data:
        line = line[:line.find("\r\n")]
        line = line.replace(" ―","")
        name = get_grp_name(line)
        if( name != None ):
            grp_index = len(name)
            grp_name = name[grp_index-1]
        fnc_name = get_fnc_name(line)
        if( fnc_name != None ):
            # print("\t"+str(fnc_name))
            for i in range(0,len(fnc_name),2):
                print("  " + fnc_name[i] + " => {")
                print("    group => \""+ grp_name +"\",")
                print("    group_index => "+ str(grp_index) +",")
                print("    bit_index => "+ ",")
                print("    reg_index => "+ ",")
                print("    value => "+ str(int(i/2)) +",")
                print("    bit_len=> "+ ",")
                print("  },")

def get_fnc_name(line):
    fnc_num = line.rfind("    ")
    if(fnc_num > -1):
        fnc_name = line[fnc_num+4:]
        fnc_name = fnc_name.split(" ")
        return fnc_name

def get_grp_name(line):
    grp_num = line.rfind("sel_")
    if(grp_num > -1):
        grp_name = line.split(" ")
        return grp_name

def get_val_name(line):
    pass

main()


















