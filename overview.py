import os

overview = open("overview.md", "w")

overview.write("The following table provides an overview of all Security Reviews and associated work found in this repo, along with a link to the report of the security review.\n\n")
overview.write("|Project/Product|Review Date|Facilitated By|")
overview.write("\n|-|-|-|")

for root, dirs, files in os.walk("./reviews"):
    path = root.split(os.sep)
    for review_file in files:
        review_full_path = "/".join(path) + "/" + review_file
        print()
        print(review_full_path)

        yaml = dict()
        yaml_started = False
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
                property_name = line_list[0]
                property_value = "".join(line_list[1:])
                if property_name in yaml:
                    yaml[property_name].append(property_value)
                else:
                    yaml[property_name] = [property_value]

            print(yaml)

            overview.write("\n|")
            overview.write(path[-1] + "|")

            review_date = ""
            facilitated_by = ""

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
                    
            overview.write(review_date + "|")
            overview.write(facilitated_by + "|")


overview.close()