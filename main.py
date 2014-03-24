import os
import optparse

def extract(dir, url, ext):
    file_names = []
    for root, dirs, files in os.walk(dir):
        for f in files:
            if f.endswith("." + ext):
                relDir = os.path.relpath(root, dir)
                if relDir != dir:
                    file_names.append(url + os.path.join(relDir, f))
                else:
                    file_names.append(url + f)


    return file_names

def save(files):
    file = open('files.txt', 'w')
    for f in files:
        file.write(f + "\n")

def main():
    parser = optparse.OptionParser(usage="usage: %prog [options] path", version = '%prog version 1.0')
    parser.add_option('-d', '--dir', help ='Directory for the search')
    parser.add_option('-u', '--url', help = 'URL which will be added as a sufix')
    parser.add_option('-e', '--extension', help = 'File extension without dot')

    (opts, args) = parser.parse_args()
    dir = opts.dir
    url = opts.url
    ext = opts.extension

    files = extract(dir, url, ext)
    save(files)


if __name__ == '__main__':
    main()