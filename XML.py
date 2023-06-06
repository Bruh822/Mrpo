from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET


class XMLRepository(ABC):
    @abstractmethod
    def add(self, element):
        pass

    @abstractmethod
    def get_by_id(self, element_id):
        pass


class UserXMLRepository(XMLRepository):
    def __init__(self, xml_file_path):
        self.xml_file_path = xml_file_path

    def add(self, user):
        tree = ET.parse(self.xml_file_path)
        root = tree.getroot()
        user_element = ET.Element("user")
        user_element.set("id", str(user.user_id))
        user_element.set("name", user.name)
        user_element.set
