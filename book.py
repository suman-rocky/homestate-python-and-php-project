#!C:\Python38-32\python.exe
print("content-type:text/html\r\n\r\n")
import cgi
import mysql.connector
form=cgi.FieldStorage()
db=mysql.connector.connect(host="localhost",user="root",passwd="",db="prop_sdf")
cur=db.cursor()
a=int(form.getvalue('id'))
cur.execute("select * from prop_detail where id=%d"%(a))
r=cur.fetchone()
print("""
<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Required meta tags-->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="Colorlib Templates">
    <meta name="author" content="Colorlib">
    <meta name="keywords" content="Colorlib Templates">

    <!-- Title Page-->
    <title>User Registration</title>

    <!-- Icons font CSS-->
    <link href="vendor/mdi-font/css/material-design-iconic-font.min.css" rel="stylesheet" media="all">
    <link href="vendor/font-awesome-4.7/css/font-awesome.min.css" rel="stylesheet" media="all">
    <!-- Font special for pages-->
    <link href="https://fonts.googleapis.com/css?family=Poppins:100,100i,200,200i,300,300i,400,400i,500,500i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

    <!-- Vendor CSS-->
    <link href="vendor/select2/select2.min.css" rel="stylesheet" media="all">
    <link href="vendor/datepicker/daterangepicker.css" rel="stylesheet" media="all">

    <!-- Main CSS-->
    <link href="css/main.css" rel="stylesheet" media="all">
</head>

<body>
    <div class="page-wrapper bg-gra-02 p-t-130 p-b-100 font-poppins">
        <div class="wrapper wrapper--w680">
            <div class="card card-4">
                <div class="card-body">
                    <h2 class="title">Registration Form</h2>
                    <form action="book_code.py">
                        <div class="row row-space">
                            
                                    <input class="input--style-4" type="hidden" name="a1" value="%d">
                               
                            <div class="col-2">
                                <div class="input-group">
                                    <label class="label">Name</label>
                                    <input class="input--style-4" type="text" name="a2">
                                </div>
                            </div>
                        </div>
                        
							<div class="row row-space">
                            <div class="col-2">
                                <div class="input-group">
                                    <label class="label">Email</label>
                                    <input class="input--style-4" type="text" name="a3">
                                </div>
                            </div>
							<div class="col-2">
                                <div class="input-group">
                                    <label class="label">Phone Number</label>
                                    <input class="input--style-4" type="text" name="a4">
                                </div>
                            </div>
							
                        <div class="p-t-15">
                            <input class="btn btn--radius-2 btn--blue" type="submit">
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    <!-- Jquery JS-->
    <script src="vendor/jquery/jquery.min.js"></script>
    <!-- Vendor JS-->
    <script src="vendor/select2/select2.min.js"></script>
    <script src="vendor/datepicker/moment.min.js"></script>
    <script src="vendor/datepicker/daterangepicker.js"></script>

    <!-- Main JS-->
    <script src="js/global.js"></script>

</body><!-- This templates was made by Colorlib (https://colorlib.com) -->

</html>
<!-- end document-->
"""%(r[0]))