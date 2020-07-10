# Your code here


# given file paths, return if query word is in the file path
#split the files after /
# put last word into cache

#ez pz 
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    cache = {}
    result = []
    for paths in files:
    
        #split after /
        separate_after_slashes = paths.split("/")
   
        last_word_in_file_path = separate_after_slashes[-1]

        if last_word_in_file_path not in cache:
            cache[last_word_in_file_path] = []

        cache[last_word_in_file_path].append(paths)

    

    for query in queries:
        if query in cache:
            result.extend(cache[query])
    return result

  


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
