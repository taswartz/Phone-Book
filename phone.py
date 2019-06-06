import csv
import string

tracker = {}

def main():
    read_input()
    in_file = 'queries.txt'
    out_file = 'output.txt'
    handle_query(in_file, out_file)
    return
    """
    while (True):
        in_file = input("\nPress Enter to Finish\n\n\tOr\n\nEnter new Filename\n")
        if in_file == '':
            break
        handle_query(in_file, out_file)
    """


def read_input():
    """Reads in input."""
    p_read = csv.reader(open('phone_dataset.csv'))
    num = 1
    for row in p_read:
        contact = row[0].split('\t')
        
        # First Last, 1119998888, NY
        if contact[3] == '':
            name = contact[0].split(' ')
            num = '(' + contact[1][0:3] + ')' + ' ' + contact[1][3:6] + '-' + contact[1][6:10]
            contact_info = [name[1], name[0], contact[2], num]
            inserter(contact_info)
            
        # First, Last, (111) 444-8888, NY
        elif contact[2][0] == '(':
            contact_info = [contact[1], contact[0], contact[2], contact[3]]
            inserter(contact_info)

        # Last, First, NY, (111) 443-9898
        elif contact[3][0] == '(':
            inserter(contact)

        else:
            print("Error: Improper Format")


def inserter(contact):
    """Inserts item into tracker dictionary."""
    l_name = contact[0].lower()
    if l_name not in tracker:
        tracker[l_name] = [contact]

    else:
        tracker[l_name].append(contact)


def handle_query(in_file, out_file):
    """Returns rows of contact information with matching name."""
    search = open(in_file, 'r')
    out_f = open(out_file, 'w+')
    for name in search:
        name = name.split()[0]
        print("Matches for: {}".format(name), file = out_f)
        num = 1
        name = name.lower()
        if name not in tracker:
            print("No Results Found", file = out_f)
            continue
        for info in tracker[name]:
            print("Result {}: {}".format(num, ', '.join(info)), file = out_f)
            num += 1


if __name__=='__main__':
    main()