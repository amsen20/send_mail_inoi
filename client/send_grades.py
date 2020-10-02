import smtplib, xlrd, sys
from email.message import EmailMessage

with open("header.txt", 'r') as f:
    header_template = f.read()
with open("each_problem.txt", 'r') as f:
    each_problem_template = f.read()
with open("footer.txt", 'r') as f:
    footer_template = f.read()

def get_mail(head, row):
    msg = [header_template.format(row[2], row[1])]
    msg += [each_problem_template.format(head[i], row[i]) for i in range(5, len(row))]
    msg += [footer_template]
    msg = "\n".join(msg)
    return row[4], msg


def send_mails():
    wb = xlrd.open_workbook(sys.argv[1])
    sheet = wb.sheet_by_index(0)

    head = sheet.row_values(0)

    for row_ind in range(1, sheet.nrows):
        try:
            row = sheet.row_values(row_ind)
            address, message = get_mail(head, row)
            msg = EmailMessage()
            msg.set_content(message)

            msg['Subject'] = 'نمرات آزمون فاینال تئوری دوره تابستانی المپیاد کامپیوتر سال ۹۹'
            msg['From'] = sys.argv[2]
            msg['To'] = address
            print(msg)
            s = smtplib.SMTP('localhost')
            s.send_message(msg)
            s.quit()
        except Exception as e:
            print("error in sending row {} which is {}!".format(row_ind, str(e)))
            try:
                print("error was for {} {} student!".format(row[2], row[1]))
            except Exception as e:
                print(str(e))


if __name__ == '__main__':
    send_mails()
