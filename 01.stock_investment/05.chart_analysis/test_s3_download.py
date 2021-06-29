# coding: utf-8

import boto3

##################################################
# メイン
##################################################
if __name__ == '__main__':
    
    BUCKET_NAME = ''
    OBJECT_NAME1 = 'data_j.csv'
    FILE_NAME1 = 'data_j.csv'
    OBJECT_NAME2 = 'PIL3.8.zip'
    FILE_NAME2 = 'PIL3.8.zip'
    OBJECT_NAME3 = 'test/test.txt'
    FILE_NAME3 = 'text.txt'
    
    # The download_file method
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, OBJECT_NAME1, FILE_NAME1)
    
    # The download_fileobj method 
    s3 = boto3.client('s3')
    with open(FILE_NAME2, 'wb') as f:
        s3.download_fileobj(BUCKET_NAME, OBJECT_NAME2, f)
    
    s3 = boto3.resource('s3')
    s3.Bucket(BUCKET_NAME).download_file(OBJECT_NAME3, FILE_NAME3)