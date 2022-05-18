if __name__ == "__main__":
    import sys
    import urllib
    import urllib.request
    import tarfile
    import os

    if len(sys.argv) < 2:
        print("No arguments given")
        pass

    command = sys.argv.pop(1)

    if command == "download_knowledge_base":
        print("DOWNLOADING STUFF...")
        FILE_URL = "https://wikidatafiles.nyc3.digitaloceanspaces.com/Hosting/Hosting/SpacyEntityLinker/datafiles.tar.gz"

        OUTPUT_TAR_FILE = '/content/wikidb_filtered.tar.gz'
        OUTPUT_DB_PATH = '/content/'
        if not os.path.exists(OUTPUT_DB_PATH):
            os.makedirs(OUTPUT_DB_PATH)
        urllib.request.urlretrieve(FILE_URL, OUTPUT_TAR_FILE)

        tar = tarfile.open(OUTPUT_TAR_FILE)
        tar.extractall(OUTPUT_DB_PATH)
        tar.close()

        os.remove(OUTPUT_TAR_FILE)
