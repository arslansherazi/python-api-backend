													/* JS of Bus Ticket Reservation System */
													
													/* JS of Bus Ticket Reservation System */

		function validateLoginPage()
		{
			var user=document.forms["login_page"]["user"].value;
			var pass=document.forms["login_page"]["password"].value;

			var token;
			
			var u,p;
			
			if(user==null || user=="")
			{
				var msg=document.getElementById("user_label");
				msg.innerHTML="*User ID is Required";
				u=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("user_label");
				msg.innerHTML="";
			}
			
			
			if(pass==null || pass=="")
			{
				var msg=document.getElementById("pass_label");
				msg.innerHTML="*Password is Required";
				p=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("pass_label");
				msg.innerHTML="";
			}
			
			
			if(u==1)
				document.login_page.user.focus();
			else 
				if(p==1)
					document.login_page.password.focus();
			
			
			if(token==1)
				return false;
			else
				return true;
		}
		
		
		
		function validateLoginHeader()
		{
			var user=document.forms["header_form"]["user"].value;
			var pass=document.forms["header_form"]["password"].value;

			var token;
			
			var u,p;
			
			if( (user==null || user=="") && (pass==null || pass==""))
			{
				alert("User ID & Password are Required");
				u=1;
				token=1;	
			}
			
			else if(user==null || user=="")
			{
				alert("User ID is Required");
				u=1;
				token=1;	
			}
			
			else if(pass==null || pass=="")
			{
				alert("Password is Required");
				p=1;
				token=1;	
			}
			
			if(u==1)
				document.header_form.user.focus();
			else 
				if(p==1)
					document.header_form.password.focus();
			
			if(token==1)
				return false;
			else
				return true;
		}
		
		
		
		
		function validateRegisterForm()
		{
			var user=document.forms["register_form"]["user"].value;
			var pass=document.forms["register_form"]["pass"].value;
			var cpass=document.forms["register_form"]["cpass"].value;
			var name=document.forms["register_form"]["name"].value;
			var email=document.forms["register_form"]["email"].value;
			var contact=document.forms["register_form"]["contact"].value;
			var male=document.forms["register_form"]["male"].checked;
			var female=document.forms["register_form"]["female"].checked;
			
			var token;
			var pass_token;
			
			var u,p,cp,n,e,c;
			
			if(user==null || user=="")
			{
				var msg=document.getElementById("userid_label");
				msg.innerHTML="User ID is Required";
				u=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("userid_label");
				msg.innerHTML="";
			}
			
			if(pass==null || pass=="")
			{
				var msg=document.getElementById("password_label");
				msg.innerHTML="Password is Required";
				token=1;
				p=1;
				pass_token=1;
			}
			else
			{
				var msg=document.getElementById("password_label");
				msg.innerHTML="";
			}
			
			if(cpass==null || cpass=="")
			{
				var msg=document.getElementById("cpassword_label");
				msg.innerHTML="Please type your password again";
				token=1;
				cp=1;
				pass_token=1;
			}
			else
			{
				var msg=document.getElementById("cpassword_label");
				msg.innerHTML="";
			}
			
			if(name==null || name=="")
			{
				var msg=document.getElementById("name_label");
				msg.innerHTML="Name is Required";
				n=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("name_label");
				msg.innerHTML="";
			}
			
			if(email==null || email=="")
			{
				var msg=document.getElementById("email_label");
				msg.innerHTML="Email is Required";
				e=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("email_label");
				msg.innerHTML="";
			}
			
			if(contact==null || contact=="")
			{
				var msg=document.getElementById("contact_label");
				msg.innerHTML="Contact No is Required";
				c=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("contact_label");
				msg.innerHTML="";
			}
			
			if( !(male) && !(female))
			{
				var msg=document.getElementById("gender_label");
				msg.innerHTML="Please select your gender";
				token=1;
			}
			else
			{
				var msg=document.getElementById("gender_label");
				msg.innerHTML="";
			}
			
			
			if(u==1)
				document.register_form.user.focus();
			else 
				if(p==1)
					document.register_form.pass.focus();
			else
				if(cp==1)
					document.register_form.cpass.focus();
			else
				if(n==1)
					document.register_form.name.focus();
			else
				if(e==1)
					document.register_form.email.focus();
			else
				if(c==1)
					document.register_form.contact.focus();
				
				
			if(pass_token!=1)
			{
				if(document.register_form.pass.value!=document.register_form.cpass.value)
				{
					var msg=document.getElementById("cpassword_label");
					msg.innerHTML="Password does not match";
					document.register_form.cpass.focus();
					token=1;
				}
			}
			
	
			if(token==1)
				return false;
			else 
				return true;
		}
		
		
		
		
		function validateFeedbackForm()
		{
			var name=document.forms["feedback_form"]["name"].value;
			var email=document.forms["feedback_form"]["email"].value;
			var contact=document.forms["feedback_form"]["contact"].value;
			var feedback=document.forms["feedback_form"]["feedback"].value;
			
			var token;
			
			var n,e,c,f;
			
			if(name==null || name=="")
			{
				var msg=document.getElementById("name_label");
				msg.innerHTML="Name is Required";
				n=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("name_label");
				msg.innerHTML="";
			}
			
			if(email==null || email=="")
			{
				var msg=document.getElementById("email_label");
				msg.innerHTML="Email is Required";
				e=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("email_label");
				msg.innerHTML="";
			}
			
			if(contact==null || contact=="")
			{
				var msg=document.getElementById("contact_label");
				msg.innerHTML="Contact No is Required";
				c=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("contact_label");
				msg.innerHTML="";
			}
			
			if(feedback==null || feedback=="")
			{
				var msg=document.getElementById("feedback_label");
				msg.innerHTML="Please write feedback";
				f=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("feedback_label");
				msg.innerHTML="";
			}
			
			
			if(n==1)
				document.feedback_form.name.focus();
			else 
				if(e==1)
					document.feedback_form.email.focus();
			else
				if(c==1)
					document.feedback_form.contact.focus();
			else
				if(f==1)
					document.feedback_form.feedback.focus();
			
			
			if(token==1)
				return false;
			else
				return true;
		}
		
		
		
		function validateFriendForm()
		{
			var name=document.forms["friend_form"]["name"].value;
			var email=document.forms["friend_form"]["email"].value;
			var fname=document.forms["friend_form"]["fname"].value;
			var femail=document.forms["friend_form"]["femail"].value;
			
			var token;
			
			var n,e,fn,fe;
			
			if(name==null || name=="")
			{
				var msg=document.getElementById("name_label");
				msg.innerHTML="Name is Required";
				n=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("name_label");
				msg.innerHTML="";
			}
			
			if(email==null || email=="")
			{
				var msg=document.getElementById("email_label");
				msg.innerHTML="Email is Required";
				e=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("email_label");
				msg.innerHTML="";
			}
			
			if(fname==null || fname=="")
			{
				var msg=document.getElementById("fname_label");
				msg.innerHTML="Your Friend's name is Required";
				fn=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("fname_label");
				msg.innerHTML="";
			}
			
			if(femail==null || femail=="")
			{
				var msg=document.getElementById("femail_label");
				msg.innerHTML="Your Friend's email is required";
				fe=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("femail_label");
				msg.innerHTML="";
			}
			
			
			if(n==1)
				document.friend_form.name.focus();
			else 
				if(e==1)
					document.friend_form.email.focus();
			else
				if(fn==1)
					document.friend_form.fname.focus();
			else
				if(fe==1)
					document.friend_form.femail.focus();
			
			if(token==1)
				return false;
			else
				return true;
		}
		
		
		
		function validateNewBusForm()
		{
			var f=document.forms["newBus_form"]["fro"].value;
			var t=document.forms["newBus_form"]["to"].value;
			var date=document.forms["newBus_form"]["date"].value;
			var dept=document.forms["newBus_form"]["dept"].value;
			var arri=document.forms["newBus_form"]["arri"].value;
			
			var token;
			
			var u,p,cp,n,e;
			
			if(f==null || f=="")
			{
				var msg=document.getElementById("from_label");
				msg.innerHTML="Location is Required";
				u=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("from_label");
				msg.innerHTML="";
			}
			
			if(t==null || t=="")
			{
				var msg=document.getElementById("to_label");
				msg.innerHTML="Location is Required";
				token=1;
				p=1;
			}
			else
			{
				var msg=document.getElementById("to_label");
				msg.innerHTML="";
			}
			
			if(date==null || date=="")
			{
				var msg=document.getElementById("date_label");
				msg.innerHTML="Date is Required";
				token=1;
				cp=1;
			}
			else
			{
				var msg=document.getElementById("date_label");
				msg.innerHTML="";
			}
			
			if(dept==null || dept=="")
			{
				var msg=document.getElementById("dept_label");
				msg.innerHTML="Departure time is Required";
				n=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("dept_label");
				msg.innerHTML="";
			}
			
			if(arri==null || arri=="")
			{
				var msg=document.getElementById("arri_label");
				msg.innerHTML="Arrival time is Required";
				e=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("arri_label");
				msg.innerHTML="";
			}
			
			
			if(u==1)
				document.newBus_form.fro.focus();
			else 
				if(p==1)
					document.newBus_form.to.focus();
			else
				if(cp==1)
					document.newBus_form.date.focus();
			else
				if(n==1)
					document.newBus_form.dept.focus();
			else
				if(e==1)
					document.newBus_form.arri.focus();
			
	
			if(token==1)
				return false;
			else 
				return true;
		}
		
		
		
		
		function validateNewFareForm()
		{
			var f=document.forms["newFare_form"]["fro"].value;
			var t=document.forms["newFare_form"]["to"].value;
			var fare=document.forms["newFare_form"]["fare"].value;
		
			
			var token;
			
			var u,p,cp;
			
			if(f==null || f=="")
			{
				var msg=document.getElementById("from_label");
				msg.innerHTML="Location is Required";
				u=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("from_label");
				msg.innerHTML="";
			}
			
			if(t==null || t=="")
			{
				var msg=document.getElementById("to_label");
				msg.innerHTML="Location is Required";
				token=1;
				p=1;
			}
			else
			{
				var msg=document.getElementById("to_label");
				msg.innerHTML="";
			}
			
			if(fare==null || fare=="")
			{
				var msg=document.getElementById("fare_label");
				msg.innerHTML="Fare is Required";
				token=1;
				cp=1;
			}
			else
			{
				var msg=document.getElementById("fare_label");
				msg.innerHTML="";
			}
			
			
			
			if(u==1)
				document.newFare_form.fro.focus();
			else 
				if(p==1)
					document.newFare_form.to.focus();
			else
				if(cp==1)
					document.newFare_form.fare.focus();
	
			if(token==1)
				return false;
			else 
				return true;
		}
		
		
		
		
		
		function validateNewPass()
		{
			var old=document.forms["ChangePass"]["old"].value;
			var newpass=document.forms["ChangePass"]["neww"].value;
			var cnew=document.forms["ChangePass"]["cnew"].value;
			
			var token=0;
			var pass_token;
			
			var u,p,cp;
			
			if(old==null || old=="")
			{
				var msg=document.getElementById("old_label");
				msg.innerHTML="Old Password Required";
				u=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("old_label");
				msg.innerHTML="";
			}
			
			if(newpass==null || newpass=="")
			{
				var msg=document.getElementById("new_label");
				msg.innerHTML="Password is Required";
				token=1;
				p=1;
				pass_token=1;
			}
			else
			{
				var msg=document.getElementById("new_label");
				msg.innerHTML="";
			}
			
			if(cnew==null || cnew=="")
			{
				var msg=document.getElementById("cnew_label");
				msg.innerHTML="Please type your password again";
				token=1;
				cp=1;
				pass_token=1;
			}
			else
			{
				var msg=document.getElementById("cnew_label");
				msg.innerHTML="";
			}
			
			
			if(u==1)
				document.ChangePass.old.focus();
			else 
				if(p==1)
					document.ChangePass.neww.focus();
			else
				if(cp==1)
					document.ChangePass.cnew.focus();
				
				
			if(pass_token!=1)
			{
				if(document.ChangePass.neww.value!=document.ChangePass.cnew.value)
				{
					var msg=document.getElementById("cnew_label");
					msg.innerHTML="Password does not match";
					document.ChangePass.cnew.focus();
					token=1;
				}
			}
			
	
			if(token==1)
				return false;
			else 
				return true;
		}
		
		
		
		function refresh()
		{
			document.getElementById("userid_label").innerHTML = "";
			var pId = document.getElementById("user").value;
			if(pId.length=="" || pId==null)
			{
				document.getElementById("userid_label").innerHTML = "User ID is Empty";
			}
			else
			{
           		 $.getJSON("/Guest/checkUsername",{u:pId},function (data)
				 {
					if (data == "yes")
					{
						document.getElementById("userid_label").innerHTML = "User ID already exists";
					}
					else
						document.getElementById("userid_label").innerHTML = "User ID is available";
            	});
			}
		}


		function validateProfileForm()
		{
			var name=document.forms["register_form"]["name"].value;
			var email=document.forms["register_form"]["email"].value;
			var contact=document.forms["register_form"]["contact"].value;
			var male=document.forms["register_form"]["male"].checked;
			var female=document.forms["register_form"]["female"].checked;

			var token;
			
			var n,e,c;

			if(name==null || name=="")
			{
				var msg=document.getElementById("name_label");
				msg.innerHTML="Name is Required";
				n=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("name_label");
				msg.innerHTML="";
			}

			if(email==null || email=="")
			{
				var msg=document.getElementById("email_label");
				msg.innerHTML="Email is Required";
				e=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("email_label");
				msg.innerHTML="";
			}

			if(contact==null || contact=="")
			{
				var msg=document.getElementById("contact_label");
				msg.innerHTML="Contact No is Required";
				c=1;
				token=1;
			}
			else
			{
				var msg=document.getElementById("contact_label");
				msg.innerHTML="";
			}

			if( !(male) && !(female))
			{
				var msg=document.getElementById("gender_label");
				msg.innerHTML="Please select your gender";
				token=1;
			}
			else
			{
				var msg=document.getElementById("gender_label");
				msg.innerHTML="";
			}



			if(n==1)
					document.register_form.name.focus();
			else
				if(e==1)
					document.register_form.email.focus();
			else
				if(c==1)
					document.register_form.contact.focus();


			if(token==1)
				return false;
			else
				return true;
		}
			
		
		//JS of Loader
		var myVar;

		function myFunction() 
		{
			myVar = setTimeout(showPage, 2000);
		}

		function showPage()
		{
			document.getElementById("loader").style.display = "none";
			document.getElementById("myDiv").style.display = "block";
		}													