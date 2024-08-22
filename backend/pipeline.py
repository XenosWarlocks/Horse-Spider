class DataCleaningPipeline:
    def process_files(self, item, spider):
        # removing extra white space
        item['content'] = item['content'].strip()
        return item