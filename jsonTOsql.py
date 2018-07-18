#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Written by: Jason Mayberry
##############################################################################
#                                                                       ###### 
#C:> cd  to the present working directory of the .json file             ######
#        that you want to convert into SQL. Make sure a copy            ######
#        of jsonTOsql.py is in the same present working directory.      ######
#        Then change the file name below to your:                      ######
#        file_name.json                                                 ######
#                                                                       ######
##############################################################################
#___ _________|-----------------\#############################################
path_to_json = 'all_tools.json'   #<<<:Change file name Here ##
##############\_________________|#### between the quotation marks. ###########
##############################################################################
# pwd "C:\Users\jason\properties\"
# Example of how to reach json values:
#  INPUT >>> origJson[5]['url']
# OUTPUT >>> ['http://pdrfinessetools.com/By%20Design/Roof%20Tools/9']
##############################################################################

import json
# import unicodedata
origJson = json.load(open(path_to_json), encoding="UTF-8")

tableName = 'all_finesse_tools'
col_1 = 'product_title'
col_2 = 'price'
col_3 = 'description'
col_4 = 'product_code'
col_5 = 'image_urls'
col_6 = 'url'
col_7 = 'project'
col_8 = 'spider'
col_9 = 'server'
col_10 = 'date'

i=0; lenList=len(origJson)
while i < lenList:
    jd1=str(origJson[i][col_1])
    v1=jd1[2:-2].strip()
    jd2=str(origJson[i][col_2])
    v2=jd2[2:-2].strip()
    jd3=str(origJson[i][col_3])
    v3=jd3[2:-2].strip()
    jd4=str(origJson[i][col_4])
    # One example of removing empty sets:
    # if 'Product Code:' not in jd4:
    #     print('Statement Omited: Missing Product Code:  ' + jd4)
    #     i += 1
    #     continue

    # In this case I was able to add Product Code: where it was missing
    if 'Product Code:' not in jd4:
        v4 = 'Product Code:  ' + v1[0:12]
        print('Statement Missing Product Code,  Was:   ' + jd4)
        v4p = str([i])
        v4ps = int(v4p[1:-1]) + 1
        print('Product Code Replaced With:            ' + v4 + '  on line # ' + str((v4ps)))
        print('\n')
    else:    
        v4=jd4[2:-2].strip()
    jd5=str(origJson[i][col_5])
    v5=jd5[2:-2].strip()
    jd6=str(origJson[i][col_6])
    v6=jd6[2:-2].strip()
    jd7=str(origJson[i][col_7])
    v7=jd7[2:-2].strip()
    jd8=str(origJson[i][col_8])
    v8=jd8[2:-2].strip()
    jd9=str(origJson[i][col_9])
    v9=jd9[2:-2].strip()
    jd10=str(origJson[i][col_10])
    v10=jd10[2:-2].strip()

    a = "INSERT INTO `" + tableName + "` (`"
    b = col_1 + "`,`" + col_2 + "`,`" + col_3 + "`,`" + col_4 + "`,`" + col_5 + "`,`" + col_6 + "`,`" + col_7 + "`,`" + col_8 + "`,`" + col_9 + "`,`" + col_10
    c = "`) VALUES ('"
    d = v1 + "','" + v2 + "','" + v3 + "','" + v4 + "',\"'"
    e = v5 #<-- an example of a mutli-value column using an extra escaped \" on each outer end of the mutli-value data
    f = "'\",'" + v6 + "','" + v7 + "','" + v8 + "','" + v9 + "','" + v10
    g = "');"
    # concatenate all the strings above into one MySQL INSERT statement
    pre_Process = a+b+c+d+e+f+g
    # do all of the pre-processing that you can
    pre_Process = pre_Process.replace(' ', ' ') # Replace all weird half spaces that map to '\u00a0'
    pre_Process = pre_Process.replace('  ', ' ') # Replace all weird half spaces that map to '\u00a0\u00a0'
    pre_Process = pre_Process.replace(" ", " ") # Replace all weird half spaces that map to '\xa0' but they still show up in the output on Windows ugh
    pre_Process = pre_Process.replace('° ', ' degree ') # Replace all
    pre_Process = pre_Process.replace(' ° ', ' degree ') # Replace all
    pre_Process = pre_Process.replace(' °', ' degree ') # Replace all
    pre_Process = pre_Process.replace('°', ' degree ') # Replace all
    pre_Process = pre_Process.replace("Don\'t", "Don\\'t") # Replace all
    pre_Process = pre_Process.replace("don\'t", "don\\'t") # Replace all
    pre_Process = pre_Process.replace("It\'s", "It\\'s") # Replace all
    pre_Process = pre_Process.replace("it\'s", "it\\'s") # Replace all
    pre_Process = pre_Process.replace("You\'re", "You\\'re") # Replace all
    pre_Process = pre_Process.replace("you\'re", "you\\'re") # Replace all
    pre_Process = pre_Process.replace("Ike\'s", "Ike\\'s") # Replace all
    pre_Process = pre_Process.replace("John\'s", "John\\'s") # Replace all
    pre_Process = pre_Process.replace("\'related products\'", "\\'related products\\'") # Replace all
    pre_Process = pre_Process.replace("product\'s", "product\\'s") # Replace all
    
    # Two examples of our json data.
    # slow bend with a 70\u00b0 3 1/2\" kick.\u00a0 Thin shaved and rounded\u00a0tip\u00a0which
    # tapered flags.\u00a0\u00a0With a \u00a0slow bend thin\u00a0shaved 9\" back from the tip,

    insert_statement = pre_Process # .decode('ascii', 'ignore') # If .decode is to be used, import unicodedata will also need to be uncommented
    # insert_statement = unicodedata.normalize("NFKD", pre_Process) # The results of this normalize can be unexpected

    newSQL = open('finesse_data.sql', 'a', encoding="UTF-8")
    newSQL.write(insert_statement + '\n')
    # OUTPUT EXAMPLE:
    # INSERT INTO `all_finesse_tools` (`product_title`,`price`,`description`,`product_code`,`image_urls`,`url`,`project`,`spider`,`server`,`date`) VALUES ('#09-  72" Long 3/4" Flip Tip Roof Rod','$250.00','72" long Interchangable flip tip roof rod. \xa0Made out of the 3/4" rod. It is very stiff and great for reaching across SUV or mini van roofs. With the flip\xa0of your wrist you will have two tools at your disposal and with the interchangable tips you will have any two tools you want. Great roof rod, comes with 2 tips, and excepts 5/16\' 18 thread count (Industry standard) tips. ','Product Code: 9',"'http://pdrfinessetools.com/image/cache/catalog/new%20tools/09%20whole-250x250.jpg', 'http://pdrfinessetools.com/image/cache/catalog/new%20tools/9-150x150.jpg', 'http://pdrfinessetools.com/image/cache/catalog/new%20tools/09%20tip-150x150.jpg'",'http://pdrfinessetools.com/By%20Design/Roof%20Tools/9','properties','manual2','DESKTOP-U4HKUI7','2018-07-14 12:39:48');
    i += 1

newSQL.close()