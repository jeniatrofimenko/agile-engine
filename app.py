import sys
from collections import Counter
from copy import copy

from bs4 import BeautifulSoup


class SmartHTMLAnalyzer:
    def __init__(self, origin_file_path, other_sample_file_path, id_name):
        self.origin_file_obj = self.parse_html_to_object(origin_file_path)
        self.other_file_obj = self.parse_html_to_object(other_sample_file_path)
        self.origin_html_elem = self.origin_file_obj.find(attrs={'id': id_name})
        self.origin_tag_name = self.origin_html_elem.name
        self.origin_tag_attrs = self.origin_html_elem.attrs

    @staticmethod
    def parse_html_to_object(path):
        """
        Parse html to object using BeautifulSoup lib
        :param path:
        :return: object
        """
        with open(path) as file:
            parsed_html_object = BeautifulSoup(file.read(), 'html.parser')

        return parsed_html_object

    def find_most_suitable_tag(self, list_of_tags):
        """
        Find tag with max number of coincidences of attrs with the origin tag
        :param list_of_tags:
        :return: object
        """
        counter = Counter()
        for i in range(len(list_of_tags)):
            for key, value in list_of_tags[i].attrs.items():
                if self.origin_tag_attrs.get(key) == value:
                    counter[i] += 1
        indx_of_the_most_common_tag = counter.most_common(1)[0][0]

        common_components = [f"{k}: {v}" for k, v in self.origin_tag_attrs.items()
                             if self.origin_tag_attrs.get(k) == list_of_tags[indx_of_the_most_common_tag].attrs.get(k)]
        print(f"Tag is chosen because it has the biggest amount of common components such as: {common_components}\n")

        return list_of_tags[indx_of_the_most_common_tag]

    def find_parents_of_the_element(self, elem):
        """
        Find parents of the tag and their indexes
        :param elem:
        :return: str
        """
        result = []

        if not elem.parent.name == "[document]":
            number_of_previous_siblings = len(elem.find_previous_siblings())
            parent = elem.parent.name
            if elem.parent.name not in ["body", "html"]:
                path_to_element = f"{parent}[{number_of_previous_siblings}]"
            else:
                path_to_element = parent
            result.append(path_to_element)
            result += self.find_parents_of_the_element(elem.parent)
        return result

    @staticmethod
    def generate_path(elem, parents):
        """
        Generate path to the tag
        :param elem:
        :param parents:
        :return:
        """
        list_of_tags = list(copy(reversed(parents)))
        list_of_tags.append(elem.name)
        path = "> ".join(list_of_tags)
        return path

    def find_html_tag_path(self):
        """
        Find path to the most suitable tag to input id
        :return:
        """
        other_file_tags_list = self.other_file_obj.find_all(self.origin_tag_name)
        result_tag = self.find_most_suitable_tag(other_file_tags_list)
        result_tag_parents = self.find_parents_of_the_element(result_tag)
        result_tag_path = self.generate_path(result_tag, result_tag_parents)
        return result_tag_path


if __name__ == "__main__":
    input_origin_file_path, input_other_sample_file_path, origin_id_name = sys.argv[1:]
    analyzer = SmartHTMLAnalyzer(input_origin_file_path, input_other_sample_file_path, origin_id_name)
    print(analyzer.find_html_tag_path())
