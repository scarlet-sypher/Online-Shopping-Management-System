
##==============Online Shopping Management System============================

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("              Welcome to MeMeZone India's Largest Shopping Website              ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

import mysql.connector as mydb
con=mydb.connect(host='localhost',user='ayush',passwd='oopplleevveell',database='online__shopping')
mycursor=con.cursor()

#=========================<login_customer>=====================================


def login():
    print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
    print('Enter "A" if you already have an account ?')
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print('Enter "B" if you are a New User?? and Sign Up!!')
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print('Enter "C" to return to the main menu!!')
    print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
    n=input("Enter A/B to proceed Futher :")

    if n.lower()=="a":

        x=input("Enter Your User ID to Login :")
        y=input("ENTER Passward :")
        print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••••")

        query="select * from login where customer_id='{x1}' and pass='{y0}'".format(x1=x,y0=y)
        mycursor.execute(query)
        z=mycursor.fetchone()
        
        if z!=None:

            query="select name from login where customer_id='{x1}' and pass='{y0}'".format(x1=x,y0=y)
            mycursor.execute(query)
            z=mycursor.fetchone()
            for i in z:
                print("===========================Welcome to MeMeZone",i,"===========================")
                print("How can we help you ?")


            #==========================================<search product>=========================================

            def search():


                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                h=input("Enter Product you want to search!!! :")
                if h.isalpha()==True:
                    query="select nop,price,nos,brand,category,p_code from product where nop='{h1}'".format(h1=h)
                    mycursor.execute(query)
                    j=mycursor.fetchall()
                    if j==[]:
                        print("Sorry Product Not Avaliable")
                        
                       
                    elif j!=None:

                        for i in j:
                            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                            print("Name of Product >>>",i[0])
                            print("Price of Product >>>",i[1])
                            print("Product Code >>>",i[5])
                            print("Name of Saller >>>",i[2])
                            print("Category of Product >>>",i[4])
                            print("Brand of Product >>>",i[3])
                            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                        l_menu()

                        
                    else:
                        print("Oops!! something went wrong")
                        l_menu()
                else:
                    print("Please use alphabets value")
                    l_menu()
                    print("\n \n")

            #==========================================</search product>=========================================


            #==========================================<Filters>=========================================

            def f_filters():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")


                
                #==========================================<range search>=========================================
                def rangee():

                    print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
                    g=input("Enter the name of your Product")
                    if g.isalpha()==True:
                        b=int(input("Enter the mininum price"))
                        v=int(input("Enter the maxmimum amount"))
                        query="select*from product where nop='{g2}' and price between {b1} and {v4}".format(g2=g,b1=b,v4=v)
                        mycursor.execute(query)
                        j=mycursor.fetchall()
                        if j==[]:
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            print("Sorry Product dosen't Found")
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            f_filter()
                            

                        elif j!=None:
                            for i in j:
                                
                                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                                print("Name of Product >>>",i[0])
                                print("Price of Product >>>",i[1])
                                print("Product Code >>>",i[5])
                                print("Name of Saller >>>",i[2])
                                print("Category of Product >>>",i[4])
                                print("Brand of Product >>>",i[3])
                                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                            f_filter()
                    else:
                        print("Please use Alphabets for name")
                        f_filter()

                #==========================================</range search>=========================================

                #==========================================<low search>=========================================
                def low():

                    print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
                    g=input("Enter the name of your Product")
                    if g.isalpha()==True:
            
                        query="select*from product where nop='{g2}' order by price".format(g2=g)
                        mycursor.execute(query)
                        j=mycursor.fetchall()
                        if j==[]:
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            print("Sorry Product dosen't Found")
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            f_filter()
                            

                        elif j!=None:
                            for i in j:
                                
                                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                                print("Name of Product >>>",i[0])
                                print("Price of Product >>>",i[1])
                                print("Product Code >>>",i[5])
                                print("Name of Saller >>>",i[2])
                                print("Category of Product >>>",i[4])
                                print("Brand of Product >>>",i[3])
                                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

                            f_filter()

                    else:
                        print("Please use Alphabets for name")
                        f_filter()


                #==========================================</low search>=========================================

                #==========================================<high search>=========================================
                def high():

                    print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
                    g=input("Enter the name of your Product")
                    if g.isalpha()==True:
            
                        query="select*from product where nop='{g2}' order by price desc".format(g2=g)
                        mycursor.execute(query)
                        j=mycursor.fetchall()
                        if j==[]:
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            print("Sorry Product dosen't Found")
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            f_filter()
                            

                        elif j!=None:
                            for i in j:
                                
                                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                                print("Name of Product >>>",i[0])
                                print("Price of Product >>>",i[1])
                                print("Product Code >>>",i[5])
                                print("Name of Saller >>>",i[2])
                                print("Category of Product >>>",i[4])
                                print("Brand of Product >>>",i[3])
                                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

                            f_filter()
                    else:
                        print("*************Please use Alphabets for name**********************")
                        f_filter()


                #==========================================</high search>=========================================

                #==========================================<category search>=========================================
                def cat():

                    print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
                    n=input("Enter Category you want to browse on :")
                    if n.isalpha()==True:
                        query="select*from product where category ='{n1}'".format(n1=n)
                        mycursor.execute(query)
                        j=mycursor.fetchall()
                        if j==[]:
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            print("NO SUCH RESULT FOUND")
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            f_filter()


                        else:
                            for i in j:
                                
                                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                                print("Name of Product >>>",i[0])
                                print("Price of Product >>>",i[1])
                                print("Product Code >>>",i[5])
                                print("Name of Saller >>>",i[2])
                                print("Category of Product >>>",i[4])
                                print("Brand of Product >>>",i[3])
                                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

                            f_filter()
                    else:
                        print("*************Please use Alphabets for name**********************")
                        f_filter()


                #==========================================</category search>=========================================

                


                def f_filter():
                    print("╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸")
                    print("\n")
                    print("➊ ➔ Want to enter the price range of the product to search")
                    print("➋ ➔ Want to see the Lowest Price First ?")
                    print("➌ ➔ Want to see the Highest Price First ?")
                    print("➍ ➔ Want to search using product category ?")
                    print("➎ ➔ Want to return to the previous menu ?")
                    print("➏ ➔ Want to return to the main menu ?")
                    print("➐ ➔ Want to Exit the Program ?")
                    print("\n")
                    print("╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸╸")
                    
                    u=int(input("Enter your Choice :"))
                    
                        
                    if u==1:
                        rangee()
                    elif u==2:
                        low()
                    elif u==3:
                        high()
                    elif u==4:
                        cat()
                    elif u==5:
                        l_menu()

                    elif u==6:
                        main_menu()
                    elif u==7:
                        exit
                      
                    else:
                        f_filters()

                f_filter()


            #==========================================</Filters>=========================================

            #==========================================<ALL>=========================================

            def All():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
                
                query="select*from product"
                mycursor.execute(query)
                j=mycursor.fetchall()
                if j==[]:
                    print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                    print("NO SUCH RESULT FOUND")
                    print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                    l_menu()
                        


                else:
                    for i in j:
                            
                        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                        print("Name of Product >>>",i[0])
                        print("Price of Product >>>",i[1])
                        print("Product Code >>>",i[5])
                        print("Name of Saller >>>",i[2])
                        print("Category of Product >>>",i[4])
                        print("Brand of Product >>>",i[3])
                        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    l_menu()




           #==========================================</ALL>=========================================

           #==========================================<buy>=========================================

            def buy():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
                
                print("Do you want to buy a product ?")
                ans="y"
                

                a=x#####id
                b=y#####passward
                while ans.lower()=="y":

                    c=input("Enter Code of product :")
                    query="select nop,price,brand,category from product where p_code='{c1}'".format(c1=c)
                    mycursor.execute(query)
                    z=mycursor.fetchall()
                    k=c
                    if z==[]:
                        print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                        print("Product code dosen't exist")
                        print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")

                    else:
                        for i in z:

                            d=i[0]
                            e=i[1]
                            f=i[2]
                            g=i[3]

                            query1="select name from login where customer_id='{a1}' and pass='{b1}'".format(a1=a,b1=b)
                            mycursor.execute(query1)
                            z1=mycursor.fetchall()
                            for j in z1:

                                p=j[0]

                                q=int(input("Enter total numbeer of quantity :"))
                                
                                
                            

                                query2="insert into bill(customer_id,qyt,name,bnop,bprice,pbrand,bcategory,pro_code)values('{}','{}','{}','{}','{}','{}','{}','{}')".format(a,q,p,d,e,f,g,k)
                                mycursor.execute(query2)
                                con.commit()
                                print("ordered successfully!!")
                        print("+---------------------------------------+")
                        ans=input("Do you want to buy more ? :")
                                

                            

                while ans.lower()=='n':
                    print("Thanks for buying")
                    print("................................................")
                    break
                    
                            
                            

                l_menu()
                            

                #==========================================</buy>=========================================

            #==========================================<bill>=========================================

            def bill():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                ans="y"
                while ans.lower()=="y":
                    a=x
                    b=y

                    query1="select contact_no from login where customer_id='{a1}' and pass='{b1}'".format(a1=a,b1=b)
                    mycursor.execute(query1)
                    z1=mycursor.fetchall()
                    for j in z1:
                        p=j[0]



                        query="select B.customer_id,B.qyt,B.name,B.bnop,B.bprice*B.qyt as Tprice,B.pbrand,B.bcategory,B.bprice,date(now()),l.contact_no,l.email_id,l.address from bill b,login l where b.name=l.name and contact_no='{k1}' and pass='{g1}'".format(k1=p,g1=b)

                        mycursor.execute(query)
                        z=mycursor.fetchall()
                        if z==[]:
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            print("NO Product Ordered!!! So no bill found!!")
                            print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                            l_menu()

                        else:

                            for i in z:
                                print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬MemeZone▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                                print("•••••••••••• CASH •••••••••••••••••▉••••••••••••••••••• MEMO •••••••••")
                                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

                                print("Your Customer ID ->",i[0])
                                print("Your Name ->",i[2])
                                print("Product Name ->",i[3],",",i[5])
                                print("Product Price -.",i[7])
                                print("Product Quantity ->",i[1])
                                print("Product Category ->",i[6])
                                print("Email ID ->",i[10])
                                print("Date of Bill Issued ->",i[8])
                                print("COntact Number ->",i[9])
                                print("Address ->",i[11])
                                print("Total Price ->",i[4])

                                print("Your Product would be delivered within 5 days")
                                print("Thanks for chossing us!!!!")
                                print("\n")
                                print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
                                print("\n")
                            l_menu()

            #==========================================</bill>=========================================


            #==========================================<cancle>========================================

            def cancle():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                a=x
                b=y
                
                u=input("Do You Really want to cancel your product ? :")
                if u.lower()=="y":
                    s=input("Enter Product Code You want to Cancel :")

               
                    
                    query="delete from bill where customer_id='{a1}' and pro_code='{s1}'".format(a1=a,s1=s)
                    mycursor.execute(query)
                    con.commit()
                    print("•••••••••••••••••••••••••••••••••••••••••")
                    print("Order Canclled!!!")
                    print("•••••••••••••••••••••••••••••••••••••••••")
                    l_menu()

                else:
                    print("•••••••••••••••••••••••••••••••••••••••••")
                    print("Wise Choice!!!")
                    print("•••••••••••••••••••••••••••••••••••••••••")

                    l_menu()

                
            

                
            #==========================================</cancle>========================================

            #==========================================<l_delete>=======================================

            def l_delete():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                print("Do you want to DELETE your ID?")
                o=x
                p=y
                query="select*from login where customer_id='{o1}' and pass='{p8}'".format(o1=o,p8=p)

                mycursor.execute(query)
                data=mycursor.fetchall()
                if data!=None:
                    n=input("you are abiut to delete your account permanently. Do you want to continue?(Y/N) :")
                    if n.upper()=="Y":
                        o=x
                        query="delete from bill where customer_id='{o1}'".format(o1=o)
                        queryy="delete from login where customer_id='{o1}'".format(o1=o)
                        mycursor.execute(query)
                        mycursor.execute(queryy)
                        con.commit()
                            
                        print("Your Account HAs been DEleted Permanenty............")
                        print("WE HOPE TO SEE YOU AGAIN!!!")
                        print("BEST REGARDS BY MEMEZONE")
                        l_menu()
                    elif n.upper()=="N":
                        print("Welcome Back")
                        l_menu()
                    else:
                        print("Oop! Wrong Choice...")
                        l_menu()
                else:
                    print("SORRY NO SUCH SELLER EXIST ON MEMEZONE  :)..............PLEASE LOGIN TO CONTINUE")
                    main_menu()


                
            #==========================================</l_delete>=======================================

            #==========================================<r_name>=======================================

            def r_name():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                n=x
                m=y
                query="select*from login where customer_id ='{n1}' and pass='{m1}'".format(n1=n,m1=m)
                mycursor.execute(query)
                data=mycursor.fetchall()
                v=input("Do you really want to change your Account details!!!    (y/n) :")
                if v.lower()=="y":
                    if data!=None:

                        f=input("Enter your new Name :")
                        if (f.isalpha() or f.isspace())==True:
                            print("Enter name correctly")
                            l_menu()

                        else:
                            g=input("Enter your new phone no :")
                            h=input("Enter your new email id :")
                            i=input("Enter your new Address :")
                            
                            query="update login set name='{f1}',contact_no='{g2}',email_id='{h3}',address='{i1}' where customer_id='{n1}' and pass='{m1}'".format(m1=m,f1=f,g2=g,h3=h,n1=n,i1=i)
                            mycursor.execute(query)
                            con.commit()
                            print("DETAIL UPDATED!!!!!!!!!!!!!!!!")

                        l_menu()
                    
                elif n.lower()=="n":
                    l_menu()

                else:
                    print("oops!! worong character entered !!!")
                    l_menu()

            #==========================================</r_name>=======================================

            #==========================================<c_pass>=======================================

            def c_pass():


                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                n=x
                m=y
                query="select*from login where customer_id ='{n1}' and pass='{m1}'".format(n1=n,m1=m)
                mycursor.execute(query)
                data=mycursor.fetchall()
                if data!=None:

                    f=input("Enter new password :")
                    
                    query="update login set pass='{f1}' where customer_id='{n1}' and pass='{m1}'".format(m1=m,f1=f,n1=n)
                    mycursor.execute(query)
                    h=con.commit()
                    print("Password Chaged Successfully!!!!!!!!!!!!!!!")
                    
                l_menu()


            #==========================================</c_pass>=======================================
                

                

            #========================================<Customer Login Menu>==================================================

            def l_menu():

                print("☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷")
                print("\n")
                print("➊ ➔ Search a Product")
                print("➋ ➔ Search using Filter's")
                print("➌ ➔ Check all the Product Avaliable")
                print("➍ ➔ Buy a Product")
                print("➎ ➔ Generate Your Bill")
                print("➏ ➔ Cancle Your Product")
                print("➐ ➔ Edit Your Account Information")
                print("➑ ➔ Want to change your passward ??")
                print("➒ ➔ Delete your Account Permanently")
                print("➓ ➔ Log Out?")
                print("\n")
                print("☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷")
                n=int(input("Enter the number according to your choice :"))

                if n==1:
                    search()
                elif n==2:
                    f_filters()
                elif n==3:
                    All()
                elif n==4:
                    buy()
                elif n==5:
                    bill()
                elif n==6:
                    cancle()
                elif n==7:
                    r_name()
                elif n==8:
                    c_pass()
                elif n==9:
                    l_delete()
                elif n==10:
                    main_menu()
                else:
                    print("oops!!! wrong choice selected")
            l_menu()
                
            #========================================</Customer Login Menu>==================================================
            
        elif z==None:
            print("Wrong passward entered Please Try Again..")
            print("••••••••••••••••••••••••••••••••••••••••••••••••")
            login()

        
    elif n.lower()=="b":
        print("You are one step closer to Sign Up for FREE!!")
        print("Please Fill The Required Fields as pre your Knowledge")
        print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••")
        print("Note:- Coloums marked with * should not be left blank")
        print("•••••••••••••••••••••••••••••••••••••••••••••••••••••••")

        o=input("Create Your Own Customer ID with misture of alphabets and numbers example(xy67)* :")
        if (o.isalpha() or o.isdigit())==True:

            print("Please Enter a valid ID in the combination of alphabet and number")
            login()
            
        else:
            
            print("ID accepted")
                
            p=input("Enter your Full Name* :")
            q=int(input("Enter your Contact Number* :"))
            r=input("Enter your Emial ID :")
            s=input("Enter a devilary address* :")
            z=input("Enter a Passward* :")
                                    
            query="insert into login(customer_id,name,contact_no,email_id,address,pass)values('{}','{}','{}','{}','{}','{}')".format(o,p,q,r,s,z)
            mycursor.execute(query)
            con.commit()

            print("Account Created Thank You For Signning Up!")
            print("•••••••••••••••••••••••••••••••••••••••••••••••••••••")
            print("Please Sign in Now!!!")
            login()

        

    elif n.lower()=="c":

        main_menu()

    else:
        print("oop's You have enter another character \nPlease Try again")
        main_menu()        


#=========================================</login_customer>================================================

#=========================================<login_seller>==================================================


def login_s():

    print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
    print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
    print('Enter "A" if you already have an account ?')
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print('Enter "B" if you are a New Saller?? and Sign Up!!')
    print("⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃⁃")
    print('Enter "C" to return to the main menu!!')
    print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
    n=input("Enter A/B to proceed Futher :")

    if n.lower()=="a":

        x=input("Enter Your Saller ID :")
        y=input("ENTER Passward :")
        print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

        query="select * from seller where s_code='{x1}' and pass='{y0}'".format(x1=x,y0=y)
        mycursor.execute(query)
        z=mycursor.fetchone()
        if z!=None:

            query="select saller_name from seller where s_code='{x1}' and pass='{y0}'".format(x1=x,y0=y)
            mycursor.execute(query)
            z=mycursor.fetchone()
            for i in z:
                print("===========================Welcome to MeMeZone",i,"===========================")
                print("How can we help you ?")

            
            #=========================================<sell_product>===================================================
    


            def sell_product():
                print("☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷▏▏You are now going to sell your products on MeMeZone▏▏☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷☷")
                
                    
                    
                    
                
##                s="select saller_name from seller where s_code='{t1}'".format(t1=t)
                
                t=x
                s=input("Enter Seller Nmae")
                if (s.isalpha() and s.isspace())==True:
                    print("use alphabet")
                    s_menu()

                else:
                    c='y'
                    while c.lower()=='y':
                        o=input("Create Your Own Product ID with misture of alphabets and numbers example(xy67)* -->")
                        if (o.isalpha() or o.isdigit())==True:

                            print("Please Enter a valid ID in the combination of alphabet and number")
                            s_menu()
                        else:
                            print("ID Accepted")

                            p=input("Enter name of your product -->")
                            q=input("Enter brand of your product -->")
                            r=input("Enter your product category (men/women/kid/household/other) -->")
                            z=input("Enter Price of product -->")
                            query="insert into product(s_code,nos,p_code,nop,brand,category,price)values('{}','{}','{}','{}','{}','{}','{}')".format(t,s,o,p,q,r,z)
                            mycursor.execute(query)
                            con.commit()
                            c=input("WANT TO ADD MORE OF YOURS ITEM??? PRESS Y/y TO CONTINUE")
                            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                            

                        while c.lower()=='n':
                            print("THANKS FOR VISITING HOPE TO SEE YOU AGAIN")
                            s_menu()
                            break
               
        #=========================================</sell_product>================================================

        #========================================<modify items>==================================================
            def mod_item():


                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                print("WANT TO UPDATE A ITEM THAT YOU SELL???")
                n=input("Enter Product Code")
                query="select*from product where p_code ='{n1}'".format(n1=n)
                mycursor.execute(query)
                data=mycursor.fetchall()
                if data!=None:
                    v=x
                    f=input("Enter NEW name of your product :")
                    g=input("Enter NEW product  brand :")
                    h=input("Enter NEW product category :")
                    k=int(input("Enter NEW price :"))
                    query="update product set nop='{f1}',brand='{g2}',category='{h3}',price='{k1}' where p_code='{n1}' and s_code='{v1}'".format(v1=v,f1=f,g2=g,h3=h,k1=k,n1=n)
                    mycursor.execute(query)
                    con.commit()
                    print("ITEM DETAIL UPDATED!!!!!!!!!!!!!!!!")
                    s_menu()
                else:
                    print("Sorry no such Product Found!!!!!!!!!!!.............PLEASE LOGIN TO CONTINUE")
                    main_menu()


          #========================================</modify items>==================================================


          #========================================<romove products>==================================================
            def remove():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                print("Do you want to DELETE a product?")
                o=x
                p=y
                query="select*from seller where saller_name='{o1}' and pass='{p8}'".format(o1=o,p8=p)

                mycursor.execute(query)
                data=mycursor.fetchall()
                if data!=None:
                    
                    
                    q=input("Enter the prouct code you want to delete :")
                    query="delete from product where p_code='{q8}' and s_code='{o1}'".format(q8=q,o1=o)
                    mycursor.execute(query)
                    con.commit()
                    print("PRODUCT DELETED !!!!!!!!!!")
                    print("WE HOPE TO SEE YOU AGAIN!!!")
                    print("BEST REGARDS BY MEMEZONE")
                    s_menu()
                else:
                    print("SORRY NO SUCH SELLER EXIST ON MEMEZONE  :)..............PLEASE LOGIN TO CONTINUE")
                    main_menu()



            #========================================</romove products>================================================
            #========================================</remove seller>==================================================

            def s_delete():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
                print("Do you want to DELETE your Saller ID?")
                o=x
                p=y
                query="select*from seller where saller_name='{o1}' and pass='{p8}'".format(o1=o,p8=p)

                mycursor.execute(query)
                data=mycursor.fetchall()
                if data!=None:
                    n=input("you are abiut to delete your account permanently. Do you want to continue?(Y/N) :")
                    if n.upper()=="Y":
                        o=x
                        query="delete from product where s_code='{o1}'".format(o1=o)
                        queryy="delete from seller where s_code='{o1}'".format(o1=o)
                        mycursor.execute(query)
                        mycursor.execute(queryy)
                        con.commit()
                            
                        print("Your Account HAs been DEleted Permanenty............")
                        print("WE HOPE TO SEE YOU AGAIN!!!")
                        print("BEST REGARDS BY MEMEZONE")
                        login_s()
                    elif n.upper()=="N":
                        print("Welcome Back")
                        s_menu()
                    else:
                        print("Oop! Wrong Choice...")
                        s_menu()
                else:
                    print("SORRY NO SUCH SELLER EXIST ON MEMEZONE  :)..............PLEASE LOGIN TO CONTINUE")
                    main_menu()


           #========================================</remove seller>==================================================

           #========================================<check list>==================================================

            def check():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                u=x
                v=y
                query="select nop,price,category,brand,p_code,nos from product where s_code='{u1}'".format(u1=u)
                mycursor.execute(query)
                j=mycursor.fetchall()
                for i in j:
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                    print("Name of Product >>>",i[0])
                    print("Price of Product >>>",i[1])
                    print("Product Code >>>",i[5])
                    print("Name of Saller >>>",i[2])
                    print("Category of Product >>>",i[4])
                    print("Brand of Product >>>",i[3])
                    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
                s_menu()

                
           #========================================</check list>==================================================

           #========================================<Change Account Details>==================================================


            def acc():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                n=x
                m=y
                query="select*from seller where s_code ='{n1}' and pass='{m1}'".format(n1=n,m1=m)
                mycursor.execute(query)
                data=mycursor.fetchall()
                if data!=None:

                    f=input("Enter your new Name :")
                    h=input("Enter your new email id :")
                    
                    query="update seller set saller_name='{f1}',email='{h3}' where s_code ='{n1}' and pass='{m1}'".format(m1=m,f1=f,h3=h,n1=n)
                    mycursor.execute(query)
                    con.commit()
                    print("DETAIL UPDATED!!!!!!!!!!!!!!!!")

                s_menu()

            #========================================</Change Account Details>==================================================

            #========================================<Change Passward>==================================================

            def sc_pass():
                

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")

                n=x
                m=y
                query="select*from seller where s_code ='{n1}' and pass='{m1}'".format(n1=n,m1=m)
                mycursor.execute(query)
                data=mycursor.fetchall()
                if data!=None:

                    f=input("Enter new password :")
                    
                    query="update seller set pass='{f1}' where s_code='{n1}' and pass='{m1}'".format(m1=m,f1=f,n1=n)
                    mycursor.execute(query)
                    h=con.commit()
                    print("Password Chaged Successfully!!!!!!!!!!!!!!!")
                    
                s_menu()


            #========================================</Change Passward>==================================================



                                                          #========================================<Saller Menu>==================================================                    
            def s_menu():

                print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
                print("\n")
                print("➊ ➜ Sell Your Product")
                print("➋ ➜ Modify YOur Product Details")
                print("➌ ➜ Remove Your Product")
                print("➍ ➜ Delete Your Saller ID")
                print("➎ ➜ Check all your Products")
                print("➏ ➜ Change your Acccount details")
                print("➐ ➜ Change your Passward")
                print("➑ ➜ Log Out?")
                print("\n")
                n=int(input("Enter the number according to your choice :"))

                if n==1:
                    sell_product()
                elif n==2:
                    mod_item()
                elif n==3:
                    remove()
                elif n==4:
                    s_delete()
                elif n==5:
                    check()
                elif n==6:
                    acc()
                elif n==7:
                    sc_pass()
                elif n==8:
                    main_menu()
                else:
                    print("oops!!! wrong choice selected")
                    s_menu()

            s_menu()
                                                        #========================================</Saller Menu>==================================================   
        else:
            print("Wrong Passward or Saller ID")
            main_menu()

    elif n.lower()=="b":
        print("You are one step closer to Sign Up for FREE!!")
        print("Please Fill The Required Fields as pre your Knowledge")
        print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")
        print("Note:- Coloums marked with * should not be left blank")
        print("▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪▪")

        o=input("Create Your Own Saller ID with misture of alphabets and numbers example(xy67)* :")
        if (o.isalpha() or o.isdigit())==True:
            print("Please Enter a valid ID in the combination of alphabet and number")
            login_s()
        else:

            print("ID accepted")
            
            p=input("Enter your Full Name* :")
            
            r=input("Enter your Emial ID :")
            
            z=input("Enter a Passward* :")
            
            query="insert into seller(s_code,saller_name,email,pass)values('{}','{}','{}','{}')".format(o,p,r,z)
            mycursor.execute(query)
            con.commit()

            print("Account Created Thank You For Signning Up!")
            print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")
            print("Please Sign in Now!!!")
            login_s()



    elif n.lower()=="c":

        main_menu()

    else:
        print("oop's You have enter another character \nPlease Try again")
        main_menu()
        
#=========================================</login_seller>==================================================

#=========================================<rating>==================================================

def rate():

    print("☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲")
    print("PLEASE HELP USE TO IMPROVE OUR SERVICE!!")
    r=5
    for i in range(r+1,0,-1):
        for j in range(0,i-1):
            print('*',end=' ')
            

        print()

    print("PLACE RATE WITH NUMBERS STAR '*'")
    i=input("ENTER THE NUMBER OF STAR")
    if i=="*":
        print("SORRY FOR DISAPPOUNTING YOU WE HOPE BEST FOR THE FUTURE")
        f=open("oo.txt","w")
        n=input("Enter your name :")
        o=input("GIVE US YOUR FEEDBACK IF YOU WANT :")
        c="name="+n+"____"+"Feedback="+o+"\n"
        f.write(c)        
        f.close()
        print("YOUR FEEDBACK WAS RECORDED!! WE WILL SURELY WORK ON IT")
        print("Thanks for visiting MeMeZone . Hope to see you again!!")
        main_menu()
    elif i=="**":
        print("SORRY FOR DISAPPOUNTING YOU WE HOPE BEST FOR THE FUTURE")
        
        f=open("Feedback.txt","w")
        n=input("Enter your name :")
        o=input("GIVE US YOUR FEEDBACK IF YOU WANT :")
        c="name="+n+"_____"+"Feedback="+o+"\n"
        f.write(c)        
        f.close()
        
        print("YOUR FEEDBACK WAS RECORDED!! WE WILL SURELY WORK ON IT")
        print("Thanks for visiting MeMeZone . Hope to see you again!!")
        main_menu()
    elif i=="***":
        print("WELL WE THINK YOU ARE FELLING GOOD AFTER VISTING US!!! WE HOPE BEST FOR THE FUTURE")
        
        f=open("Feedback.txt","w")
        n=input("Enter your name :")
        o=input("GIVE US YOUR FEEDBACK IF YOU WANT :")
        c="name="+n+"_____"+"Feedback="+o+"\n"
        f.write(c)        
        f.close()
        
        print("YOUR FEEDBACK WAS RECORDED!! WE WILL SURELY WORK ON IT")
        print("Thanks for visiting MeMeZone . Hope to see you again!!")
        main_menu()
    elif i=="****":
        print("THANKS OF BEING WUTH US WE HOPE BEST FOR THE FUTURE")
       
        f=open("Feedback.txt","w")
        n=input("Enter your name :")
        o=input("GIVE US YOUR FEEDBACK IF YOU WANT :")
        c="name="+n+"_____"+"Feedback="+o+"\n"
        f.write(c)        
        f.close()
        
        print("YOUR FEEDBACK WAS RECORDED!! WE WILL SURELY WORK ON IT")
        print("Thanks for visiting MeMeZone . Hope to see you again!!")
        main_menu()
    elif i=="*****":
        print("VERY VERY THANK YOU WE HOPE BEST FOR THE FUTURE")
        
        f=open("Feedback.txt","w")
        n=input("Enter your name :")
        o=input("GIVE US YOUR FEEDBACK IF YOU WANT :")
        c="name="+n+"_____"+"Feedback="+o+"\n"
        f.write(c)        
        f.close()
        
        
        print("YOUR FEEDBACK WAS RECORDED!! WE WILL SURELY WORK ON IT")
        print("Thanks for visiting MeMeZone . Hope to see you again!!")
        main_menu()

        f.close()
    else:
        print("invalid character emtered plz enter your * wisly")
        main_menu()





#=========================================<menu_page>================================================

def main_menu():
    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    print("➊ ➜ Are you a customer?")
    print("➋ ➜ Are you a saller?")
    print("❸ ➜ Rate our Page")
    print("➍ ➜ Quit")

    print("☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵☵")
    ch=int(input("Enter your choice :"))
    if ch==1:
        login()
    elif ch==2:
        login_s()
    elif ch==3:
        rate()
    elif ch==4:
        quit

    else:
        print("Sorry Wrong Key Entered")
        main_menu()
main_menu()
#=========================================</menu_page>================================================
