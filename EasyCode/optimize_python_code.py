'''
python scripts: file size is huge

with open("large_file.csv") as f:
    data=f.readlines()       loads entire file
'''

def read_in_chunks(file_object, chunk_size=1024 * 1024):  # 1MB chunks
    while chunk := file_object.read(chunk_size):
        yield chunk

with open("large_file.csv") as f:
    for chunk in read_in_chunks(f):
        # process chunk
        print(chunk[:100])

'''
Why this works better:

Reads one line at a time
Memory usage stays constant, no matter file size
Python file objects are already iterators, so this is efficient
File has no clear line structure
You want I/O efficiency tuning
'''