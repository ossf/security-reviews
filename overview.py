import os

overview = open("overview.md", "w")

overview.write("The following table provides an overview of all Security Reviews and associated work found in this repo, along with a link to the report of the security review.\n\n")
overview.write("|Project/Product|Review Date|Facilitated By|Issues|Methodology|Scope|Packages|")
overview.write("\n|-|-|-|-|-|-|-|")

for root, dirs, files in os.walk("./reviews"):
    path = root.split(os.sep)
    for review_file in files:
        review_full_path = "/".join(path) + "/" + review_file

        yaml = dict()
        yaml_started = False
        methodology_types = ["Static-Analysis", "Dynamic-Analysis", "Code-Review", "Web-Search", "Fuzzing", "External-Review"]
        with open(review_full_path, "r", encoding="utf8") as review:
            lines = review.readlines()
            for metadata_line in lines:
                line = metadata_line[:-1]
                if line == "---":
                    if not yaml_started:
                        yaml_started = True
                        continue
                    break
                line_list = line.split(":")
                for methodology_type in methodology_types:
                    if methodology_type in line:
                        line_list = ["Methodology", methodology_type]
                property_name = line_list[0]
                property_value = "".join(line_list[1:])
                if property_name in yaml:
                    yaml[property_name].append(property_value)
                else:
                    yaml[property_name] = [property_value]

            overview.write("\n|")
            overview.write(path[-1] + "|")

            review_date = ""
            facilitated_by = ""
            issues = ""
            methodology = ""
            scope = ""
            packages = ""

            for prop in yaml:
                if "Review-Date" in prop:
                    review_date += yaml[prop][0]
                if "Organization" in prop:
                    if facilitated_by != "":
                        facilitated_by += ", "
                    facilitated_by += ", ".join(yaml[prop])
                if "Name" in prop:
                    if facilitated_by != "":
                        facilitated_by += ", "
                    facilitated_by += ", ".join(yaml[prop])
                if "Issues-Identified" in prop:
                    issues += yaml[prop][0]
                if "Methodology" in prop:
                    methodology += ", ".join(yaml[prop])
                if "Scope" in prop:
                    scope += yaml[prop][0]
                if "pkg" in prop:
                    if len(yaml[prop]) == 1:
                        packages += "pkg:" + yaml[prop][0]

            if (len(methodology) > 2):
                methodology = methodology[2:]

            if packages == "":
                packages = "None Listed"
                    
            overview.write(review_date + "|")
            overview.write(facilitated_by + "|")
            overview.write(issues + "|")
            overview.write(methodology + "|")
            overview.write(scope + "|")
            overview.write(packages + "|")


overview.close()