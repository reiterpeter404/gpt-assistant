import os

# check if a file exists and has content
# returns true, if the file exists or has content, false otherwise
def file_exists_or_has_content(file_name):
    file_exists = os.path.exists(file_name)

    # check if file exists
    if not file_exists:
        return False

    # check if file has any content
    with open(file_name, "r") as out_file:
        if out_file.read() == "":
            return False
        else:
            return True

# a class Conversation with a list of role and content
class Conversation:
    # constructor
    # if file_name is given, the content of the file is read and stored in the list
    def __init__(self, file_name=""):
        self.role = []
        self.content = []
        self.file_name = file_name

        if self.file_name == "":
            return

        # check if file exists
        file_exists = file_exists_or_has_content(file_name)
        if not file_exists:
            return

        with open(file_name, "r") as out_file:
            content = out_file.read()
            lines = content.split("\n")

            for line in lines:
                if line.startswith("  - role: "):
                    role = line.replace("  - role: ", "")
                    self.role.append(role)
                elif line.startswith("    content: "):
                    content = line.replace("    content: ", "")
                    self.content.append(content)
                elif not line.startswith("conversation:"):
                    # get last context element
                    cnt = len(self.content) - 1
                    self.content[cnt] += "\n" + line


    # adds a new role and content to the list
    def add(self, role, content):
        self.role.append(role)
        self.content.append(content)


    # returns the list of role and content
    def to_list(self):
        return [{"role": role, "content": content} for role, content in zip(self.role, self.content)]


    # writes the content of the list to a file in yaml format
    # if the file does not exist, the file and the header are created
    def to_yaml(self, file_name):
        if self.file_name == "":
            return

        # check if file exists
        file_exists = file_exists_or_has_content(file_name)
        if not file_exists:
            with open(self.file_name, "a") as out_file:
                out_file.write("conversation:\n")

        for cnt in range(len(self.role)):
            role = self.role[cnt]
            content = self.content[cnt]

            stored_content = content.replace("\"", "\\\"")
            with open(self.file_name, "a") as out_file:
                out_file.write(f"  - role: {role}\n")
                out_file.write(f"    content: \"{stored_content}\"\n")


    # appends the last role and content to a file in yaml format
    # if the file does not exist, the file and the header are created
    def append_last_conversation_to_yaml(self):
        if self.file_name == "":
            return

        # check if file exists
        file_exists = file_exists_or_has_content(self.file_name)
        if not file_exists:
            with open(self.file_name, "a") as out_file:
                out_file.write("conversation:\n")

        # store last element
        cnt = len(self.role) - 1
        role = self.role[cnt]
        content = self.content[cnt]

        stored_content = content.replace("\"", "\\\"")
        with open(self.file_name, "a") as out_file:
            out_file.write(f"  - role: {role}\n")
            out_file.write(f"    content: \"{stored_content}\"\n")


    # adds a new role and content to the list and appends it to the file in yaml format
    # if the file does not exist, the file and the header are created
    def add_and_append_to_yaml(self, role, content):
        self.add(role, content)
        self.append_last_conversation_to_yaml()