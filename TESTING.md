# PensionPal - Testing documentation
---
*This file contains the Testing section of the [full README.md file for PensionPal](README.md).*

## Table of Contents
---
- [Testing](#testing)
  * [Code Validation](#code-validation)
  * [Test Cases - user stories](#test-cases---user-stories)
  * [Features Testing](#features-testing)
  * [Other Manual Testing](#other-manual-testing)
  * [Automated Testing](#automated-testing)
  * [Fixed Bugs](#fixed-bugs)
  * [Known Bugs](#known-bugs)
  * [Supported Screens and Browsers](#supported-screens-and-browsers)

## Testing
---
### Code Validation
- The [W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML on every page of the project. Two small errors were raised in relation to a missing `;` after the copyright entity, and a section without a `heading` element. These were rectified and all pages pass the validation check. The [results of checking each HTML page can be viewed here](docs/code-validation/html-validation.pdf).

- The [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate the project's custom CSS. [The CSS passes and the results can be viewed here](docs/code-validation/css-validation.png).

- [JSHint](https://jshint.com/) was used to check the quality of the JavaScript code and check for errors. Two `Missing semicolon` errors were rectified and there are no errors. [The results of this check can be viewed here](docs/code-validation/javascript-validation.png).

- The Python code has been validated using [PEP8 online checker](http://pep8online.com/). Errors in relation to `line too long (86 > 79 characters)` were fixed. There are no validation errors in the sumitted code for custom Python code. Django standard files have not been amended in relation to line length errors. The [results of validation each python file can be viewed here](docs/code-validation/python-validation.pdf).

### Test Cases - user stories
Note: testing of the user stories was carried out while each user story/feature was developed, to ensure acceptance criteria were met before the issue was closed. The below documents the user story testing that was completed at the end of the project.
- [#1](https://github.com/Fiona-T/pension-pal/issues/1): As a visiting user, I can learn what the site is about, so I can decide whether to sign up to the site
    * Acceptance Criteria 1:  The first thing a user should see on entering the website is an image relevant to the topic and a tagline explaining exactly what the website is for
    * Acceptance Criteria 2: There should be a Learn More button here, which will link to more detailed information
    * Acceptance Criteria 3: Below the image there should be a section briefly explaining the purpose of the website/the benefits for the user
  >**Result:** Pass, the above acceptance criteria are met, as shown below:
![User story - learn about site](docs/user-story-testing/learn-about-site.png)

- [#19](https://github.com/Fiona-T/pension-pal/issues/19): As a visiting user I can find out what I could use the website for if I signed up so that I can understand the benefits of signing up and decide whether to sign up
    * Acceptance Criteria 1:  Home page has a section "What is PensionPal?" explaining briefly what the website will help the user achieve
    * Acceptance Criteria 2: Home page has a section "Why Use PensionPal?" explaining the benefits to the user
    * Acceptance Criteria 3: Home page has a section "How to Use PensionPal?" explaining to the user how to get started and how to use the site if they sign up for an account
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - purpose of site](docs/user-story-testing/website-purpose.png)

- [#2](https://github.com/Fiona-T/pension-pal/issues/2): As a site user, I can navigate the site so that I can find the page I want to go to 
    *  Acceptance Criteria 1:  Header should be at the top of every page
    *  Acceptance Criteria 2: Logo (site name) should be prominent in the header and it links to the home page
    *  Acceptance Criteria 3:  Header contains just Sign Up, Sign In links in addition to the logo (since this is not a registered user)
  >**Result:** Pass, the above acceptance criteria are met, as seen on the screenprints for the previous user stories.

- [#18](https://github.com/Fiona-T/pension-pal/issues/18): As a registered user I can navigate the site so that I can find the page I want to go to
    * Acceptance Criteria 1:  If a user is not logged in, the header contains the logo (linked to home page) and the links to Sign In and Sign Up
    * Acceptance Criteria 2: If a user is logged in, the links in the header change: My Jobs, My Pensions, Sign Out are present and Sign Up and Sign In are no longer present.
    * Acceptance Criteria 3: Header is present on all pages as per above, and fixed to the top of the page
    * Acceptance Criteria 4: Username should be shown when user is logged in
  >**Result:** Pass, the above acceptance criteria are met as shown below (and for not signed in user, shown in previous user story).
![User story - page header naviation](docs/user-story-testing/website-purpose.png)

- [#28](https://github.com/Fiona-T/pension-pal/issues/28): As a registered user I can see which page I am on within the My Jobs pages so that I can locate myself within the pages
    *  Acceptance Criteria 1:  When a user is on the pages that link from the main My Jobs page, there is a breadcrumb sub-navigation at the top of the page 
    *  Acceptance Criteria 2: For example, a user on the Add Job page will see a breadcrumb like: My Jobs -> Add Job, with My Jobs linking back to My Jobs page
    *  Acceptance Criteria 3: The main My Jobs page does not have a breadcrumb (since it is a top level page)
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - jobs pages navigation](docs/user-story-testing/jobs-app-navigation.png)

- [#29](https://github.com/Fiona-T/pension-pal/issues/29): As a user I can see which section of the website I am on so that I know which part of the website I went into
    * Acceptance Criteria 1:  The link, in the main navigation in the header, for the page the user is currently on, is styled differently when it is the active page (except for home page as the logo serves as the home page link)
    * Acceptance Criteria 2: For pages that have 'sub' pages e.g. My Jobs has add job, success page, etc., the different styling remains in the top navigation, when the user is within these sub pages
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - current page in header](docs/user-story-testing/current-page-in-header.png)

- [#52](https://github.com/Fiona-T/pension-pal/issues/52): As a registered I can see the title of the page I am on in the browser window so that I know which page I have open
    * Acceptance Criteria 1:  The relevant page title is displayed in the browser toolbar
    * Acceptance Criteria 2:  The title is specific to the page the user is currently on
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - page title](docs/user-story-testing/page-title.png)

- [#3](https://github.com/Fiona-T/pension-pal/issues/3): As a registered user, I can sign into my account so that I can access my jobs and pension information
    * Acceptance Criteria 1:  The page to sign in opens after clicking Sign In from the site header
    * Acceptance Criteria 2: The sign in page contains the username and password fields to sign in with, and sign in button
    * Acceptance Criteria 3: After signing in, the user is redirected to the My Jobs page
    * Acceptance Criteria 4: there is a note on the sign in page directing the user to the Sign Up page if they have not previously created an account
  >**Result:** Pass, the above acceptance criteria are met as shown below, and page redirects to My Jobs after sign in.
![User story - sign in page](docs/user-story-testing/sign-in-page.png)

- [#4](https://github.com/Fiona-T/pension-pal/issues/4): As a registered user, I can sign out of my account when finished, so that I know I am signed out securely
    * Acceptance Criteria 1:  When a user is signed in, the Sign Out link is present in the header
    * Acceptance Criteria 2: After clicking the Sign Out link, the Sign Out page opens
    * Acceptance Criteria 3: Sign Out page has text asking user to confirm they want to sign out, and a button
    * Acceptance Criteria 4: after signing out, the user is redirected to the home page and the header reflects the status of a user who is not logged in, i.e. only contains the Sign In and Sign Up links and not My Jobs/My Pensions/Sign Out
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - sign out](docs/user-story-testing/sign-out.png)

- [#25](https://github.com/Fiona-T/pension-pal/issues/25): As a registered user I can cancel my sign out request so that I can easily get back to the page I was previously on 
    * Acceptance Criteria 1:  After clicking the Sign Out button, there is a button saying Cancel, as well as the Sign Out button
    * Acceptance Criteria 2: Clicking Cancel will bring the user back to the previous page they were on
  >**Result:** Pass, the above acceptance criteria are met, Cancel button on Sign Out form as shown above. And this brings the user back to the previous page.

- [#6](https://github.com/Fiona-T/pension-pal/issues/6): As a new user, I can sign up for an account so that I can start recording my jobs and pensions details
    * Acceptance Criteria 1:  The sign up page opens after clicking the Sign Up link in the header
    * Acceptance Criteria 2: Sign up page contains contains fields for the user to register with a username, email address and password and a button to submit the form
    * Acceptance Criteria 3: After submitting the form the user is brought to the My Jobs page (as they are now signed in)
    * Acceptance Criteria 4: The user can't submit the form unless all the fields have been completed
  >**Result:** Pass, the above acceptance criteria are met as shown below, and page redirects to My Jobs after sign up:
![User story - sign up](docs/user-story-testing/sign-up.png)

- [#7](https://github.com/Fiona-T/pension-pal/issues/7): As a registered user, I can record details of a job so that I can build up my employment history records
  * Acceptance Criteria 1:  A registered user can go to the My Jobs page, click Add a Job and a form is displayed for them to complete
  * Acceptance Criteria 2: The form contains fields for Employer name, date of joining, date of leaving, and whether the employment was full or part time.
  * Acceptance Criteria 3: All fields on the form are mandatory
  * Acceptance Criteria 4: After adding the employment details, the user can see these details in the My Jobs page
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add job](docs/user-story-testing/add-job.png)

- [#21](https://github.com/Fiona-T/pension-pal/issues/21) As a registered user I can see confirmation that my job details were added so that I know the form submitted correctly and there were no errors
  * Acceptance Criteria 1:  After a registered user submits the Add Job form successfully, they are redirected to a success page
  * Acceptance Criteria 2: Success page confirms the employment was added and reminds the user to now add a pension if there was a pension attached to the job
  * Acceptance Criteria 3: Success page has links to the My Jobs page where the user can view the jobs they added
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add job success](docs/user-story-testing/add-job-success.png)

- [#23](https://github.com/Fiona-T/pension-pal/issues/23): As a registered user I can add the dates to the Add Job form in the order of: day, month, year so that I know I am entering the correct date, since this is the date format used in Ireland
* Acceptance Criteria 1:  The date fields on the Add Job form accept the format in the order of d, m, y. 
* Acceptance Criteria 2: E.g. if a user enters a date of 01/05/2021, this means a date of 1st May 2021 and not 5th Jan 2021
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add job date format](docs/user-story-testing/add-job-date-format.png)

- [#24](https://github.com/Fiona-T/pension-pal/issues/24): As a registered user I can easily enter the dates when adding a job so that I can complete the form intuitively and easily
  * Acceptance Criteria 1:  The Add Job form has placeholders/helptext in the Start date and Finish date inputs
  * Acceptance Criteria 2: The placeholder/helptext shows the format of the date to use 
  *  cceptance Criteria 3: If possible a date picker is also included on these inputs so that the user can select the date more easily
  >**Result:** Pass, the above acceptance criteria are met as shown below; and user can either use the date picker to enter a date, or type into the placeholder text. It is clear to the user the date format that is being used and easy to enter a date.
![User story - add job date fields datepicker and placeholder](docs/user-story-testing/add-job-date-inputs-widget.png)

- [#42](https://github.com/Fiona-T/pension-pal/issues/42): As a registered user I can not add a new Employment with the same name as another Employment in my Jobs records so that I don't add duplicate records which would cause confusion
  * Acceptance Criteria 1:  A logged in user on the Add Job form, cannot add an Employer Name that matches the employer name of one of their existing Job records
  * Acceptance Criteria 2: If they try to do this, an error is displayed on the Add Job form explaining that the employer name already exists and to edit or delete the existing Job record, or add a different Employer name for the new record
  * Acceptance Criteria 3: The Add Job form cannot be submitted until the Employer name differs to any of that user's existing job records
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add job prevent duplicate employer name](docs/user-story-testing/add-job-duplicate-employment-check.png) 

- [#55](https://github.com/Fiona-T/pension-pal/issues/55): As a registered user I can see a relevant error message if I enter a job finish date that is before the start date so that I can correct the error before the job record is saved
  * Acceptance Criteria 1:  When adding or editing a job, if the user enters a finish date that is before the start date on the form, the job is not added
  * Acceptance Criteria 2: The form is displayed again to the user, with an error message stating what the issue is, along with the data they previously entered into the form
  * Acceptance Criteria 3: When the user corrects the error and submits the form, the job is added/edited successfully
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add job error if finish before start date](docs/user-story-testing/add-job-dates-dates-validation.png) 

- [#8](https://github.com/Fiona-T/pension-pal/issues/8): As a registered user, I can see all the jobs I have added so that I can get the overall picture of my work history
  * Acceptance Criteria 1:  When a user is logged in and on the My Jobs page, all jobs added by that user are listed here
  * Acceptance Criteria 2: The jobs added to date are shown in a section called Your Jobs
  * Acceptance Criteria 3: Each job has the Employer name (prominently), the start and end date, and whether it was full or part time
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - view jobs added](docs/user-story-testing/view-jobs.png) 

- [#22](https://github.com/Fiona-T/pension-pal/issues/22): As a registered user I can see confirmation that I have no jobs recorded so that I know I have not previously recorded any jobs and that is why there are no jobs displayed
  * Acceptance Criteria 1:  On the My Jobs page there is a note underneath Your Jobs heading confirming that the user does not have any jobs added, if that user has not previously added any jobs, or has added jobs but deleted them
  * Acceptance Criteria 2: If the user does have jobs in their records, then these are displayed and the note is not displayed
  >**Result:** Pass, the above acceptance criteria are met as shown below (and see above for when there are jobs added):
![User story - no jobs](docs/user-story-testing/view-jobs-no-jobs.png) 

- [#27](https://github.com/Fiona-T/pension-pal/issues/27): As a registered user I can view my jobs listings in shorter pages so that I can click through each page instead of scrolling through a long list of my jobs
  * Acceptance Criteria 1:  On the My Jobs page, under Your Jobs, the max number of jobs displayed is 6
  * Acceptance Criteria 2: If there are more than 6 jobs, then there is a pagination feature at the bottom of the page which allows the user to go from one page to the next/previous
  * Acceptance Criteria 3: If it is the first page of jobs, then there is only a next arrow. If it is the last page of jobs then there is only a previous arrow
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - view jobs pagination](docs/user-story-testing/view-jobs-pagination.png) 

- [#60](https://github.com/Fiona-T/pension-pal/issues/60): As a registered user I can see the pensions that are attached to a job so that I know whether there are any pensions attached or not, and can access the pensions easily if there are
  * Acceptance Criteria 1:  In the My Jobs page, the card for each job has information on whether there is a pension or pensions attached to the job
  * Acceptance Criteria 2: If there is no pension attached then a note on that job card confirms this
  * Acceptance Criteria 3: If there is a pension or pensions attached, the name of the pension scheme is shown and this is linked to the details page for that pension
  >**Result:** Pass, the above acceptance criteria are met as shown below - no pension attached, one pension attached or multiple pensions attached. Attached pensions are linked to the view full details page for each pension.
![User story - job details includes pension](docs/user-story-testing/job-card-shows-attached-pensions.png) 

- [#9](https://github.com/Fiona-T/pension-pal/issues/9): As a registered user, I can edit a job so that I can correct the previously recorded information
   * Acceptance Criteria 1:  User can click on the Edit button on the jobs list, and this brings up a form to edit the details
  * Acceptance Criteria 2: The existing details of the job are pre-populated on the form so user just needs to update the fields that are changing
  * Acceptance Criteria 3: The form contains the same fields as the Add Job form, along with a confirmation button to Confirm, or a cancel button to go back
  * Acceptance Criteria 4: After submitting the form, the user is redirected to the my jobs page
  * Acceptance Criteria 5: The job in the jobs list now shows the amended details
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - edit job](docs/user-story-testing/edit-job.png) 

- [#30](https://github.com/Fiona-T/pension-pal/issues/30): As a registered user I can only access the edit page for jobs that were added by me so that I cannot access the jobs of a different user and I know my records can't be accessed by another user 
  * Acceptance Criteria 1:  A user who is logged in and tries to access an edit job form by using a url with an id of a job they did not create, cannot access the page
  * Acceptance Criteria 2: The user is redirected to a 404 page
  * Acceptance Criteria 3: The user can still access the edit job form for their own records, using either the Edit button from the My Jobs list, or using a url with the job id in it
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - cannot access edit job page of different user](docs/user-story-testing/edit-job-other-user-job-id.png) 

- [#45](https://github.com/Fiona-T/pension-pal/issues/45): As a registered user I can see confirmation the edits to my job record were successful so that I know the changes I made have been saved
  * Acceptance Criteria 1:  A logged in user, after pressing the Confirm Changes button on the Edit Job form is returned to the My Jobs page if the form was submitted successfully (existing functionality). A message is then displayed on the My Jobs page confirming the Job record was successfully updated with the changes
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - edit job success message](docs/user-story-testing/edit-job-success-msg.png)  

- [#53](https://github.com/Fiona-T/pension-pal/issues/53): As a registered user I can click a link that brings me to the Edit Job page, from the View or Edit pages of the attached Pension so that I can go directly to the Edit page of the associated Job, instead of having to navigate to it 
  * Acceptance Criteria 1:  There is a link directly to the Edit Job page from the View Full Details page for a pension
  * Acceptance Criteria 2: There is a link directly to the Edit Job page from the Edit Pension page
  * Acceptance Criteria 3: The linked Edit Job page is to edit the job that the pension is attached to 
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - edit job links from pension details and edit pension pages](docs/user-story-testing/edit-job-links-from-pension-details.png)  

- [#10](https://github.com/Fiona-T/pension-pal/issues/10): As a registered user, I can delete a job so that I can remove it from my records if I added it in error 
  * Acceptance Criteria 1:  User can click on the Delete button on the jobs list, this brings up a confirmation page asking the user to confirm the deletion
  * Acceptance Criteria 2:  There is a cancel button (to go back to my-jobs list) and a button to confirm deletion
  * Acceptance Criteria 3: The job no longer exists in the job list after pressing the delete button
  * Acceptance Criteria 4: After pressing the delete button, the user is redirected to the my jobs page
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - delete job](docs/user-story-testing/delete-job.png) 

- [#43](https://github.com/Fiona-T/pension-pal/issues/43): As a registered user I can see confirmation a Job record was deleted after I press Delete button so that I know the record was definitely deleted
  * Acceptance Criteria 1:  A logged in user, after pressing the Delete button and then the Delete Job button on the Delete Job modal, is returned to the My Jobs page (existing functionality) A message is displayed on the My Jobs page confirming the Job record was deleted
  >**Result:** Pass, the above acceptance criteria are met as shown in the previous user story - success message displayed

- [#50](https://github.com/Fiona-T/pension-pal/issues/50): As a registered user I can only delete my own Job records so that I cannot delete the Job records of a different user and I know my records can't be deleted by another user
  * Acceptance Criteria 1:  A user who is logged in and tries to delete a job they did not create cannot do this
  * Acceptance Criteria 2:  The user is redirected to a 404 page
  * Acceptance Criteria 3:  Even the user who owns that job id cannot access the url and is redirected to a 404 page, because the delete job is done through a modal and not a separate page
  >**Result:** Pass, the above acceptance criteria are met as shown below. User can't access the delete functionality by url. They can only access through the Delete button on their own records, which then posts the deletion to the database from the delete button on the delete modal.
![User story - delete job can't access url](docs/user-story-testing/delete-job-url.png) 

- [#61](https://github.com/Fiona-T/pension-pal/issues/61): As a registered user I can see what pensions (if any) will be deleted, before I delete a Job record so that I am aware of the consequences before deleting the Job record
  * Acceptance Criteria 1:  On the delete job modal that pops up before the user presses the button to confirm the Deletion, there is information on whether there are attached pensions which would be deleted when the Job is deleted
  * Acceptance Criteria 2: If there is no pension attached then the delete job modal confirms this
  * Acceptance Criteria 3: If there is a pension or pensions attached, the name of the pension scheme is shown for information
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - delete job note if pensions attached](docs/user-story-testing/delete-job-warning-re-attached-pensions.png) 

- [#11](https://github.com/Fiona-T/pension-pal/issues/11): As a registered user, I can record the details of a pension so that I can have the pension recorded on my account
   * Acceptance Criteria 1:  A registered user can go to the My Pensions page, click Add a Pension and a form is displayed for them to complete
  * Acceptance Criteria 2: The form contains fields for Employment(dropdown list from user's previously created jobs), pension scheme name, policy no., scheme no., type of pension, salary, PAO, 20% director, pension provider, value, file upload field, additional notes.
  * Acceptance Criteria 3: All fields on the form are mandatory except member number, file upload and additional notes (PAO and Director default to false)
  * Acceptance Criteria 4: After adding the pension details, the user can see these details in the My Pensions page (this depends on [#12](https://github.com/Fiona-T/pension-pal/issues/12))
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add pension](docs/user-story-testing/add-pension.png) 

- [#36](https://github.com/Fiona-T/pension-pal/issues/36): As a registered user I can see confirmation that my pension details were added so that I know the add Pension form submitted correctly and there were no errors 
  * Acceptance Criteria 1:  After a registered user submits the Add Pension form successfully, they are redirected to a success page
  * Acceptance Criteria 2: Success page confirms the pension was added and has links to the My Pensions page if they need to edit/delete the pension
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add pension success page](docs/user-story-testing/add-pension-success.png) 

- [#39](https://github.com/Fiona-T/pension-pal/issues/39): As a registered user I know how to add a job if it does not exist in the Employment dropdown on the Add Pension form so that I can then add the pension linked to that job
  * Acceptance Criteria 1:  On the Add Pension form there is helptext underneath the 'Employment' dropdown field
  * Acceptance Criteria 2: The helptext advises the user that if the Job does not exist in the dropdown, they need to add the job
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add pension Employment field helptext](docs/user-story-testing/add-pension-job-helptext.png) 

- [#40](https://github.com/Fiona-T/pension-pal/issues/40): As a registered user I can be notified that I have no recorded Jobs when I try to Add a Pension so that I can then add the Job, since the Job needs to be added before the Pension can be added
  * Acceptance Criteria 1:  When the user does not have any Jobs recorded and clicks on the Add Pension button, the Add Pension form is not displayed (as they cannot add a pension without linking it to one of their job records)
  * Acceptance Criteria 2: Instead they are shown a notification that they do not have any jobs recorded yet
  * Acceptance Criteria 3: The notification reminds them that they need to add the job/employment first before they can add the pension, and provides the link to the add job form/ my-jobs page
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add pension Employment field helptext](docs/user-story-testing/add-pension-no-jobs.png) 

- [#47](https://github.com/Fiona-T/pension-pal/issues/47): As a registered user I can see which fields on the Add/Edit Pension form are mandatory so that I understand which fields must be completed by me and which are optional
  * Acceptance Criteria 1:  On the Add Pension and Edit Pension pages, there is a note explaining which fields are mandatory and some identifying feature on the fields (e.g. asterisk)
  * Acceptance Criteria 2:  The form can be submitted if the optional fields are left blank
  >**Result:** Pass, the above acceptance criteria are met as shown in the user story for adding a new pension record, or editing a pension record. There is a note at top of form stating that required fields are marked with an asterisk, and the asterisk is present on the required field labels. The form can be submitted if the optional fields are left blank.

- [#56](https://github.com/Fiona-T/pension-pal/issues/56): As a registered user I can know what file types I can upload when adding/editing a pension so that I can avoid uploading a file type that is not allowed
  * Acceptance Criteria 1:  On the Add Pension or Edit Pension forms, there is a note on the file field advising what file types can be uploaded
  * Acceptance Criteria 2: If the user adds a file that is not one of the allowed file types, an error is displayed on the form when trying to submit the form
  * Acceptance Criteria 3: The allowed file types are jpg and png
  >**Result:** Pass, the above acceptance criteria are met as shown below (also tested with uploading a pdf file which gives error, and uploading png file which uploads OK):
![User story - add pension File field](docs/user-story-testing/add-pension-file-upload-field.png) 

- [#59](https://github.com/Fiona-T/pension-pal/issues/59): As a registered user I can choose from a list of only the active Pension Providers on the pension provider field when adding or editing a pension so that I know that the pension provider is a current one
  * Acceptance Criteria 1:  When a user is adding a pension record, the 'Pension provider' dropdown list only contains the Pension Providers that have a status of active
  * Acceptance Criteria 2:  When a user is editing a pension record, the 'Pension provider' dropdown list only contains the Pension Providers that have a status of active
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - add or edit pension only shows active providers](docs/user-story-testing/pension-forms-active-providers.png) 

- [#12](https://github.com/Fiona-T/pension-pal/issues/12): As a registered user, I can view the pensions I have added so that I can see all my pension details in one place
  * Acceptance Criteria 1:  When a user is logged in and on the My Pensions page, all pensions added by that user are listed here
  * Acceptance Criteria 2: The pensions added to date are shown in a section called Your Pensions, with summary details shown
  * Acceptance Criteria 3: Each pension has the Scheme name, employer name and value shown, and buttons to View the full details, Edit, and Delete the pension
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - view pensions](docs/user-story-testing/view-pensions.png) 

- [#38](https://github.com/Fiona-T/pension-pal/issues/38): As a registered user I can view my pensions listings in shorter pages so that I can click through each page instead of scrolling through a long list of my pensions
  * Acceptance Criteria 1:  On the My Pensions page, under Your Pensions, the max number of pensions displayed is 6
  * Acceptance Criteria 2: If there are more than 6 pensions, then there is a pagination feature at the bottom of the page which allows the user to go from one page to the next/previous
  * Acceptance Criteria 3: If it is the first page of pensions, then there is only a next arrow. If it is the last page of pensions then there is only a previous arrow
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - view pensions - pagination](docs/user-story-testing/my-pensions-pagination.png) 

- [#13](https://github.com/Fiona-T/pension-pal/issues/13): As a registered user, I can edit a pension I previously added, so that I can correct or update the previously recorded information
  * Acceptance Criteria 1:  User can click on the Edit button on the pensions list, and this brings up a form to edit the details
  * Acceptance Criteria 2: The existing details of the pension are pre-populated on the form so user just needs to update the fields that are changing
  * Acceptance Criteria 3: The form contains the same fields as the Add Pension form, along with a confirmation button to Confirm, or a cancel button to go back
  * Acceptance Criteria 4: After submitting the form, the user is redirected to the my pensions page
  * Acceptance Criteria 5: The pension in the pensions list now shows the amended details
  >**Result:** Pass, the above acceptance criteria are met as shown below, and the page redirects to My Pensions after the form is submitted:
![User story - edit pension](docs/user-story-testing/edit-pension.png) 

- [#46](https://github.com/Fiona-T/pension-pal/issues/46): As a registered user I can see confirmation that the edits I made to my pension record were successful, so that I know the changes made have been saved
  * Acceptance Criteria 1:  A logged in user, after pressing the Confirm Changes button on the Edit Pension form is returned to the My Pensions page if the form was submitted successfully (existing functionality). A message is then displayed on the My Pensions page confirming the Pension record was successfully updated with the changes
  >**Result:** Pass, the above acceptance criteria are met as shown below, after submitting the changes in the previous user story:
![User story - edit pension success message](docs/user-story-testing/edit-pension-success-msg.png) 

- [#14](https://github.com/Fiona-T/pension-pal/issues/14): As a registered user, I can delete a pension I previously added, so that I can remove it from my records if I added it in error 
  * Acceptance Criteria 1:  User can click on the Delete button on the pensions list, this brings up a confirmation page asking the user to confirm the deletion
  * Acceptance Criteria 2: There is a cancel button (to go back to my-pensions list) and a button to confirm deletion
  * Acceptance Criteria 3: The pension no longer exists in the pension list after pressing the delete button
  * Acceptance Criteria 4: After pressing the delete button, the user is redirected to the my pensions page
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - delete pension](docs/user-story-testing/delete-pension.png) 

- [#44](https://github.com/Fiona-T/pension-pal/issues/44): As a registered user I can see confirmation that a Pension record was deleted, after I press the Delete button so that I know the record was definitely deleted
  * Acceptance Criteria 1:  A logged in user, after pressing the Delete button and then the Delete Pension button on the Delete Pension modal, is returned to the My Pensions page (existing functionality) A message is then displayed on the My Pensions page confirming the Pension record was deleted 
  >**Result:** Pass, the above acceptance criteria are met as shown in the previous user story - success message displayed

- [#49](https://github.com/Fiona-T/pension-pal/issues/49): As a registered user I can only delete my own Pension records so that I cannot delete the Pension records of a different user and I know my records can't be deleted by another user
  * Acceptance Criteria 1:  A user who is logged in and tries to delete a pension they did not create cannot do this
  * Acceptance Criteria 2: The user is redirected to a 404 page
  * Acceptance Criteria 3: Even the user who owns that pension id cannot access the url and is redirected to a 404 page, because the delete pension is done through a modal and not a separate page
  >**Result:** Pass, the above acceptance criteria are met as shown below. User can't access the delete functionality by url. They can only access through the Delete button on their own records, which then posts the deletion to the database from the delete button on the delete modal.
![User story - delete pension can't access by url](docs/user-story-testing/delete-pension-url.png) 

- [#15](https://github.com/Fiona-T/pension-pal/issues/15): As a site user, I can access external resources relating to pensions, so that I can find out more information 
  * Acceptance Criteria 1:  The links are in the footer on each page
  * Acceptance Criteria 2:  Links to be included are: The Pensions Authority (https://www.pensionsauthority.ie/en/), Revenue Commissioners (https://www.revenue.ie/en/jobs-and-pensions/pensions/index.aspx) and Citizens Information (https://www.citizensinformation.ie/en/money_and_tax/personal_finance/pensions/)
  * Acceptance Criteria 3: The links open in a new window
  >**Result:** Pass, the above acceptance criteria are met as shown below. Links are present in the footer on all pages and the links open to the correct location and in a new tab.
![User story - footer - external resources](docs/user-story-testing/footer-external-resources.png) 

- [#16](https://github.com/Fiona-T/pension-pal/issues/16): As a site user, I can find the PensionPal social media accounts, so that I can follow them on social media to keep up to date
  * Acceptance Criteria 1:  The social media icons are in the footer on each page
  * Acceptance Criteria 2: The links open in a new window
  * Acceptance Criteria 3: The links/icons are for LinkedIn, Instagram, Facebook and Twitter
  >**Result:** Pass, the above acceptance criteria are met. Links are present in the footer on all pages and the links open to the correct location and in a new tab (see previous user story for screenprint).

- [#17](https://github.com/Fiona-T/pension-pal/issues/17): As a website owner/admin I can add pension providers to a table in the admin panel so that users can select the pension provider when adding or editing a pension in My Pensions page
  * Acceptance Criteria 1:  When logged into the admin panel, the user can add a new Pension Provider
  * Acceptance Criteria 2: The details the admin user can record for the pension provider is: name, website url and status (active or not active)
  * Acceptance Criteria 3: Only the admin user can access this admin panel and Pension Provider table
  >**Result:** Pass, the above acceptance criteria are met as shown below. Only admin superuser can access the Django admin site.
![User story - admin - add provider](docs/user-story-testing/admin-add-provider.png) 

- [#32](https://github.com/Fiona-T/pension-pal/issues/32): As a website owner/admin I can edit the details for a Pension Provider so that the correct details for that Pension Provider feed through for the website users when viewing the My Pensions pages
  * Acceptance Criteria 1:  In the admin panel, the admin user can click on the Provider Name to bring them to the change form, where they can amend any details (default Django admin functionality)
  * Acceptance Criteria 2: In the admin panel, the admin user can edit the Status of the provider from the list view and press Save there, without having to go into the change form
  * Acceptance Criteria 3: In the admin panel, the admin user can edit the Website of the provider from the list view and press Save there, without having to go into the change form
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - admin - edit provider](docs/user-story-testing/admin-edit-provider.png) 

- [#33](https://github.com/Fiona-T/pension-pal/issues/33): As a website owner/admin I can view the Pension Providers list and their details in the admin panel so that I can see what Pension Providers are on the list, and find details for a specific provider
  * Acceptance Criteria 1:  In the admin panel, the admin user can click on Providers and see the pension providers listed, with their name, website and whether they are active or not
  * Acceptance Criteria 2: In the admin panel the admin user when viewing Providers can filter them by their status i.e. active/not active
  * Acceptance Criteria 3: In the admin panel, the admin user when viewing Providers can search for a provider by their name or by their website
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - admin - view providers](docs/user-story-testing/admin-view-providers.png) 

- [#34](https://github.com/Fiona-T/pension-pal/issues/34) As a website owner/admin I can delete a Pension Provider from the list so that they can be removed, if they were added in error. But cannot delete a Pension Provider if there are Pension records attached to it.
  * Acceptance Criteria 1:  An admin user in the admin site can delete a Pension Provider, if there are no pension records attached to it
  * Acceptance Criteria 2: However if there are pension records attached, the deletion is prevented because of the attached pension records
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - admin - delete providers](docs/user-story-testing/admin-delete-providers.png) 

- [#26](https://github.com/Fiona-T/pension-pal/issues/26) As a site admin I can view the date formats in the admin panel as dd/mm/yyyy so that the dates are in the format I am used to, living in Ireland
  * Acceptance Criteria 1:  When the admin user is signed into the admin panel, and views a Job, the dates shown are in the format dd/mm/yyyy and not yyyy/mm/dd
  * Acceptance Criteria 2: If the admin user goes to the Add Job form in the admin panel and adds start and finish date using the date picker, the date chosen is then displayed in the format dd/mm/yyyy
  * Acceptance Criteria 3: If the admin user goes to the Add Job form in the admin panel and types in the start and finish date in the format dd/mm/yyyy, the date saves in this same format and does not change into the American format (e.g. 01/05/2021 does not become 5th Jan 2021 
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - admin - date format](docs/user-story-testing/admin-date-format.png) 

- [#35](https://github.com/Fiona-T/pension-pal/issues/35) As a user I can see a custom 'Page not found' page when I try an access a page in error so that I can find my way back to the website and I know I have not left the website(as the branding is the same as the rest of the website)
  * Acceptance Criteria 1:  The 404 page not found displayed to the user is consistent with the branding on the rest of the website
  * Acceptance Criteria 2:  The page contains the header and footer as per the rest of the webiste
  * Acceptance Criteria 3: The page contains a note to the user stating the page was not found, and links for them to get back to the website
  >**Result:** Pass, the above acceptance criteria are met as shown below and the 404 page generates for an invalid url, or for user trying to access records of a different user by url.
![User story - custom 404 page](docs/user-story-testing/custom-404-page.png) 

- [#37](https://github.com/Fiona-T/pension-pal/issues/37) As a registered user I can view details of a Pension that I added so that I can see all of the details of the pension in full for information or to check that they are correct
  * Acceptance Criteria 1:  User can click on the View Details button on the pensions list, and this brings up a page showing the full details of that Pension
  * Acceptance Criteria 2:  All details of the Pension are displayed (except for added by), along with date of joining service, date of leaving service (from the related Job), and pension provider website (from the related Provider)
  * Acceptance Criteria 3: There are two buttons at the bottom of the page, one to Edit and one to Delete
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - view pension details](docs/user-story-testing/view-pension-details.png) 

- [#41](https://github.com/Fiona-T/pension-pal/issues/41) As a registered user I can only access the View Full Details page for pensions that were added by me so that I can't access the pension records of another user and I know my records can't be accessed by another user
  * Acceptance Criteria 1:  A user who is logged in and tries to access the view pension details page by using a url with an id of a pension they did not create, cannot access the page
  * Acceptance Criteria 2: The user is redirected to a 404 page
  * Acceptance Criteria 3: The user can still access the view details page for their own records, using the View Full Details button, or using a url with the pension id in it
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - can't view pension details of different user](docs/user-story-testing/cant-view-other-user-pension.png) 

- [#54](https://github.com/Fiona-T/pension-pal/issues/54) As a registered user I can easily view the full details of the pension I just added by clicking a link from the add pension success page so that I can check that I added all the details correctly
  * Acceptance Criteria 1:  After submitting the Add Pension form, the success page contains a link to view the full details of the pension just added 
  * Acceptance Criteria 2: The link brings the user to the Pension Details page where they can see all details of that pension, and the associated job 
  * Acceptance Criteria 3: The success page still contains a link to the My Pensions page, so the user can go here if they don't want to go to the Pension Details page
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - view pension details after adding the record](docs/user-story-testing/view-pension-after-adding.png) 

- [#64](https://github.com/Fiona-T/pension-pal/issues/64): As a registered user I can easily get back to previous page when on the Pension Details page so that I can go back to where I was in one click and not have to navigate through pages when viewing Pension Details and associated Job details
  * Acceptance Criteria 1:  There is a Back to previous page or similar on the Pension Details page, which takes the user back to whatever page they were on previously (e.g. they can come to this page from the My Jobs page and may want to go back to that page instead of to the My Pensions page in the breadcrumb)
  >**Result:** Pass, the above acceptance criteria are met as shown below, and the link brings user back to the previous page:
![User story - back to previous link on view pension details page](docs/user-story-testing/view-pension-back-link.png) 

- [#65](https://github.com/Fiona-T/pension-pal/issues/65): As a registered user I can see if the pension provider for my existing pension records is no longer active so that I can update the record to the new pension provider
  * Acceptance Criteria 1:  If the pension provider for a record is no longer active, then when a user views this record on the Pension Details, there is a note under the Pension provider details stating that the provider is no longer active and therefore the user should edit the record to update to the new active pension provider 
  * Acceptance Criteria 2: If the pension provider status is active, then there is no note on the record
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - view pension details note if provider is inactive](docs/user-story-testing/view-pension-inactive-provider.png) 

- [#57](https://github.com/Fiona-T/pension-pal/issues/57): As a registered user I can use the Cancel button on forms to go back to the previous page so that I can go back to the previous page and not a pre-determined page
  * Acceptance Criteria 1:  On the Add Job or Edit Job form, if the user presses the cancel button they are brought back to the previous page they were on (currently defaults to go back to My Jobs page, but these forms can be accessed from other pages and user may want to navigate back)
  * Acceptance Criteria 2: Similarly on the Add Pension or Edit Pension form, if the user presses the Cancel button they are brought back to the previous page they were on, and not necessarily to My Pensions, unless they were previously on My Pensions page
  >**Result:** Pass, the above acceptance criteria are met, the button is present on the forms and pressing it brings the user back to the previous page. There is a small bug which has just come to light at the end of the project: if the form has an error so the page is therefore reloaded with the error message (i.e. server side error messages), the Cancel button needs to be pressed twice to get back to the previous page. This will be noted in the [Known Bugs](#known-bugs) section, to be rectified in future iterations.
![User story - cancel button](docs/user-story-testing/cancel-button.png) 

- [#62](https://github.com/Fiona-T/pension-pal/issues/62): As an admin user I can view the job details for all users in the admin site so that I have an overview of jobs per user
  * Acceptance Criteria 1:  In the admin site, an admin user can go to Jobs and see the job records with all details (added by, employer name, start and finish dates, full/part time) in the list view
  * Acceptance Criteria 2: The admin user can filter the list by the person who added the job record
  * Acceptance Criteria 3: Clicking on the Employer Name will bring the admin user to the page showing details for that record
  * Acceptance Criteria 4: The admin user can search by the employer name in the Jobs list
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - admin - view jobs](docs/user-story-testing/admin-view-jobs.png) 

- [#63](https://github.com/Fiona-T/pension-pal/issues/63): As an admin user I can view the pension records in the admin site for all users so that I have an overview of the pensions added by the website users
 * Acceptance Criteria 1:  In the admin site, an admin user can go to Pensions and see the pension records listed under the headings added by, scheme name, employment and value
 * Acceptance Criteria 2: They can filter the list by the person who added the pension record, or by the pension provider
 * Acceptance Criteria 3: Clicking on the scheme name will bring the admin user to the page showing the full details for that pension record, along with the Id of the record for information
 * Acceptance Criteria 4: The admin user can search the pensions list by employer name and scheme name
  >**Result:** Pass, the above acceptance criteria are met as shown below:
![User story - admin - view pensions](docs/user-story-testing/admin-view-pensions.png) 

### Features Testing
Features were tested while testing the User Story test cases outlined in the preceding [Test Cases - user stories](#test-cases---user-stories) section. All relevant screenprints can be found there.

### Other Manual Testing
During development extensive manual testing was carried out. Manually tested adding, editing, deleting and viewing jobs and pension records via the frontend; and admin functions of adding, editing and deleting pension providers in the admin site. This was carried out while manually testing each user story/feature as it when it was developed. 

Verified that all links work and external links open in a new page so as not to direct user away from the site. 

**Note in relation to website addresses for Pension providers:** The pension providers that have been added during development are dummy fictional pension providers, so their websites are not actual websites and clicking on these links would result in a page not found. This would not be the case in a real life scenario, as the actual current pension providers present in Ireland would be added to the Provider table by the website owner. In addition the website owner would be responsible for maintaining the correct website address (along with the other provider details) for each provider as part of the role of maintainting the Pension Providers list.

### Automated Testing
- #### Python tests
    Automated testing was carried out on the Python code in each of the three apps. Tests were written as each feature or user story was developed in each iteration, in line with the Agile approach used for the project development. The created tests were ran and the feature was not closed until the tests passed. Tests were written for the models, views and forms.

    On completion of the project, all tests were ran again to ensure they still passed and the results of these are shown below. The tests that were written are contained in the relevant `test_forms.py`, `test_views.py` and `test_models.py` files in each app.

    - Pages app automated test results - no models or forms, so only view tests
    ![Pages app automated test results](docs/automated-testing/pages-app-automated-tests.png)

    - Jobs app automated test results - forms, models, views
    ![Jobs app automated test results](docs/automated-testing/jobs-app-automated-tests.png)

    - Pensions app automated test results - forms, models, views
    ![Pensions app automated test results](docs/automated-testing/pensions-app-automated-tests.png)

- #### Coverage
    The [coverage](https://coverage.readthedocs.io/en/6.2/) tool was used to determine the effectiveness of the tests. On the initial run, the pensions app was missing some tests and tests were added for the Add Pension and Edit Pension forms when the form is not valid, to ensure it reloads the page with the form. 

    As shown below, the final coverage report shows the pages and jobs apps both have 100% coverage, and the pensions app has 99% coverage. 

    - Pages app coverage report
    ![Pages app coverage report](docs/automated-testing/pages-app-coverage-report.png)

    - Jobs app coverage report
    ![Jobs app coverage report](docs/automated-testing/jobs-app-coverage-report.png)

    - Pensions app coverage report
    ![Pensions app coverage report](docs/automated-testing/pensions-app-coverage-report.png)
    There is one test missing for forms.py in the pensions app as shown below, however this has been tested manually and since the overall level of coverage is very close to 100% it felt reasonable to leave the tests as is.
    ![Pensions app coverage report - forms.py missing test](docs/automated-testing/pensions-forms-coverage-missing-test.png)

    To run the coverage report to see any further details, do the following in the IDE command line:
    1. install coverage: `pip3 install coverage`
    2. run coverage on specific app: `coverage run --source=appname manage.py test` e.g. for the jobs app it would be `coverage run --source=jobs manage.py test`
    4. generate the report (displays report in command line): `coverage report`
    5. generate an interactive html version of the report that can be viewed in the browser: `coverage html`
    6. view the report: `python3 -m http.server`. Open the port 8000 when it pops up, click on `htmlcov/` lin the Directory listing and then click on the specific module to see further details.

- #### JavaScript tests
    Since there is only a small amount of JavaScript code used in the project, the testing carried out for these functions was manual testing only, as part of the User Stories and Features testing described above.

### Fixed Bugs
The following bugs were encountered during development and during testing.

- **Issue: Edit Job Form not showing the existing data on the form for start date and finish date**
![Edit Job Form dates bug](docs/bugs/edit-from-dates-bug.png)
The error in the Console stated: `the specified value "06/09/2020" does not conform to the required format, "yyy-MM-dd"`
> Solution:
Amended the `widgets` setting in the `AddJobForm` in `forms.py`, for the `DateInput format` from `%d/%m/%Y` to `%Y-%m-%d` so that it matches the format expected, as [explained in this post on Stackoverflow](https://stackoverflow.com/questions/66504151/django-update-form-does-not-conform-to-the-required-format-yyyy-mm-dd). The front end still displays the desired format of dd/mm/yyyy (for Irish users) because the `LANGUAGE_CODE` had been set to `en_gb` in `settings.py`. 
- **Issue: `Add Pension Form` 'employment' field displaying all employments not just those belonging to that user**
![Pension Form 'employment' field bug](docs/bugs/add-pension-form-employment-bug.png)
When the Add Pension form was displayed to the user, it is displaying all Employments from the Job table, but these need to be filtered to only show the records added to the Job table by that user. 
> Solution: Followed the advice in this [post on Stack Overflow](https://stackoverflow.com/questions/15608784/django-filter-the-queryset-of-modelchoicefield/15608899): Instead of amending the `forms.py`, added the below to the `AddPension` view in `views.py` so that the field contains just the `Job` records added by the current user. 
```python
form.fields['employment'].queryset = Job.objects.filter(added_by=request.user)
```
- **Issue: Testing the `AddPension View`, form would not post due to incorrect data in 'employment' and 'pension_provider' fields**
![Pension Form 'employment' field bug](docs/bugs/add-pension-view-test-post-bug.png)
When testing the POST part of the `AddPension` View, the test was failing because the page was not redirecting as expected. This was because some of the form data was not valid, so the form was not posting and the page only redirects when the form is valid. 
> Solution: The issue was because of invalid data on the 'employment' and 'pension_provider' fields, which are foreign keys in the Pension model (from Job and Provider models respectively). When passing the data to post the test form, I had been passing in the relevant values from the test Job and Provider records, like the below:
```python
'employment': 'Test Company',
'pension_provider': 'A Pension Provider',
```
However, since these are foreign keys I needed to use their id instead of the actual values, as outlined in this [post on Stack Overflow](https://stackoverflow.com/questions/37393788/django-testing-a-form-is-valid-when-it-contains-a-modelchoicefield). Amended the data being passed to post the form to reference the id (which was 1 in both cases), like below, the tests then passed as the page redirected after posting the form:
```python
'employment': str(1),
'pension_provider': str(1),
```

- **Issue: File upload to Cloudinary from `PensionForm` not working**

Adding a file via the optional `file` field on the Add Pension or Edit Pension form did not give any errors and the form could be submitted, but the file did not appear when viewing the pension details on the frontend, nor did it appear in Cloudinary. When viewing the pension record in the Django admin panel, the file did not appear there either.
> Solution: On investigation with [Code Institute's](https://codeinstitute.net/ie/) tutor support, it transpired that the issue did not arise when adding a pension (with file upload) via the Django admin panel. However for this to work via the front end form, two parts were missing, as explained in the [Django docs](https://docs.djangoproject.com/en/4.0/topics/http/file-uploads/):
1. The `post` part of the `view` for posting the form needed to include `request.FILES` in the form constructor (see below), in order to record the file data:
```python
form = PensionForm(request.POST, request.FILES)
```
2. The `form` element in the relevant `html` files needed to include the `enctype` attribute with the value `"multipart/form-data"` as this is required where a file is uploaded through a form 

- **Issue: Using the delete pension or delete job url gives a 405 error instead of the custom 404 page**

Delete Pension url with valid pension id:
![Delete Pension url bug](docs/bugs/delete-pension-url-bug.png)
Delete Job url with valid job id:
![Delete Job url bug](docs/bugs/delete-job-url-bug.png)
If a user tried to access the delete url (by typing the url into the browser) for a pension or job using a valid job or pension id that belongs to that user, a 405 error is raised instead of 404 (a 404 error would be raised if they used an invalid id in the url, and the custom 404 page would be displayed).
> Solution: The 405 http error [means method not allowed](https://httpstatuses.com/405), so it is being raised because there was no `get method` on the `DeleteJob` or `DeletePension` views (there was only a `post method` to delete the record, triggered by the Delete button in the modal). Updated both views to include a `get method`, which raises a 404 error so that the user will see the custom 404 page. There is no way to access the delete url from the website, but this update was done in case a user types the url into the browser, so that they are shown the custom 404 page instead of the generic 405 error page. 

- **Issue: Unique validation for `employer_name` giving Integrity Error**
![Add Job unique constraint bug](docs/bugs/add-job-unique-check-bug.png)
In the Job model, a unique constraint was added so that [users cannot add a job record with a duplicate employer name](https://github.com/Fiona-T/pension-pal/issues/42) - this is to avoid confusion when they add a pension record, as the pension record is linked to a job and that job details, so each job record must be unique for that user. During manual testing of this change, attempting to add a duplicate job record via the Add Job page raised an Integrity Error as shown above after the form was submitted.
> Solution: On reading [the Django Forms documentation](https://docs.djangoproject.com/en/3.1/ref/forms/validation/), the problem was that the `form.is_valid()` check called in the view was passing, but the `form.save()` method was failing because the model instance failed the unique constraint check. The reason for this is because the `'added_by'` field on the model (i.e the user) is excluded in the `AddJobForm` fields (because this is automatically set and doesn't need to be completed by the user on the form) and therefore the `is_valid()` method called on the form cannot do the unique validation because one of the fields in the unique constraint is not present on the form. The `.is_valid()` check on a `ModelForm` performs `.clean_fields()`, `.clean()` and `.validate_unique()` for all fields that are included in the form. In order to raise an error on a field that is not on the form, [the Django model instances validation documentation](https://docs.djangoproject.com/en/4.0/ref/models/instances/#validating-objects) recommends overriding the `Model.clean_fields()` method. Including the `.validate_unique()` method will then validate the unique constraints on the model (instead of just on individual fields). Therefore the Job model was updated to include the below method:
```python
def clean_fields(self, exclude=None):
        super().clean_fields(exclude=exclude)
        self.validate_unique()
``` 
- **Issue: Unique validation for `employer_name` and `added_by` giving Integrity Error**
![Add Job unique constraint, 'added_by' bug](docs/bugs/add-job-unique-check-added-by-bug.png)
Following on from the above bug, even after adding the `clean_fields` method with `validate_unique`, an Integrity Error was still being raised.
> Solution: The `added_by` field was being set (`form.instance.added_by = request.user`) inside the `.is_valid()` method and was causing this issue. Moved this to be set before the `.is_valid` check is performed. 

- **Issue: AddJob form not displaying error messages or previously entered data**

After entering invalid data on the AddJob form, the record was correctly not added, but the form was returned to the user blank and without any error messages.
> Solution: The `else` part of the `if form.is_valid()` check was incorrectly creating a new instance of the AddJob form and including this with the context. Therefore a blank new form was being returned to the user. Updated the context to include the original form instance, as shown below:
![AddJob form instance bug fix](docs/bugs/add-job-new-instance-bug-fix.png)


- **Issue: JobForm unique constraint error message is generic**
![Add Job generic error message bug](docs/bugs/add-job-generic-error-msg-bug.png)
The error message displayed pulls in the name of the fields, but 'Added by' is not a field that the user would be familiar with, since this is set in the background based on the request user. A more helpful error message is needed.
> Solution: The error message is a `NON_FIELD_ERROR` set automatically by Django, however as advised in the [Django modelforms documentation](https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/), the error message can be overridden in the form `Meta` class by adding the `NON_FIELD_ERRORS key` to the `error_messages dictionary` like below (and importing `NON_FIELD_ERRORS` from `django.core.exceptions` at the top of the `forms.py` file)
```python
error_messages = {
    NON_FIELD_ERRORS: {
        'unique_together': 'You already have a Job with this Employer'
        ' name. Choose a different name for this new Job record.'
    }
}
```

- **Issue: `jobs` app `test_views` failing after unique constraint added to `Job` model**
![jobs app test_views fail after unique constraint added](docs/bugs/jobs-test-views-after-unique-constraint-bug.png)
After the `UniqueConstraint` on `'employer_name'` per user was added to the `Job` model, the `test_views.py` file for jobs app was failing, on the `setUpClass` for the `TestMyJobsListView`
> Solution: The reason it was failing was because the `setUpClass` created 20 job records, 10 for each of 2 test users (in order to test pagination on listview), but it used the same details for each job record. Therefore these records were failing the unique check for employer name, as it would be creating 10 records with same employer name for each test user. 
Updated `'employer_name'` in `objects.create` to include the job index which we had from the below:
```python
number_of_jobs = 20
for job in range(number_of_jobs):
```
in the name, as shown below, so that each name will be different:
![jobs app test_views employer_name unique constraint fix](docs/bugs/jobs-test-views-unique-constraint-fix.png)

- **Issue: File name not retained for file upload on Pension form**
![Filename bug on Pension Form](docs/bugs/pension-file-name-bug.png)
The name of the file uploaded by the user was not retained when saved in Cloudinary.
> Solution: The reason for this is [Cloudinary by default sets a random public ID for the uploaded file name](https://support.cloudinary.com/hc/en-us/articles/202520762-How-to-upload-images-while-keeping-their-original-filenames-), however this can be changed either by setting parameters on `CloudinaryFileField` in the form, or by setting an `Upload Preset` in the Cloudinary settings. Example of setting the parameters in the form (including the folder to upload the image to):
```python
file = CloudinaryFileField(
        options={
            'folder': 'media',
            'use_filename': 'true',
            'unique_filename': 'true',
        }
    )
```
I opted to use the `Upload Preset` instead of the above, setting `use_filename` to `true`, but kept the `unique_filename` parameter as `true`, so that files with the same name do not get overwritten (setting `unique_filename` to false means the filename stays as is, but then files with the same name would be overwritten). This means the file uploaded by the user retains their filename, but has randomly generated characters at the end of the filename, which is an acceptable solution to avoid any files being overwritten.

- **Issue: Error on file upload of type not accepted by Cloudinary image**
![Filetype Cloudinary error bug](docs/bugs/cloudinary-file-type-error-msg-bug.png)
When trying to upload a file type of .doc, a Server Error (500) is generated (when `Debug=False`), see above for the error message when `Debug=True`. The error is arising because the `resource_type` for the Cloudinary file is by default `'image'` (which is fine for the purposes of this project), so a .doc file is not accepted. However an error message is not generating for the user, only the server error.
> Solution: On researching this, I could not find how to override the Cloudinary error checking, in order to present an error message on the form instead of having the Server Error. So I therefore added a `.clean()` method to this field in the form, to check for the extension on the file name, and raise a ValidationError that way - so that it is displayed on the form for the user:
```python
def clean_file(self):
    data = self.cleaned_data['file']
    if data:
        filename = data.name
        if not filename.endswith(('.jpg', '.png', '.jpeg')):
            raise ValidationError(
                'File type must be .png or .jpg. Choose a different file '
                'of the correct type'
                )
    return data
```
- **Issue: HTML form validation on Add Pension or Edit Pension not showing the error messages for fields with `required` attribute**

When submitting the form without the `required` fields completed, the form correctly didn't submit, but it did not display the usual error message "Please select an item in the list" or "Please fill in this field" for the first non-completed required field. The issue happens when the first uncompleted `required` field is outside of the viewport when the submit button is pressed. It doesn't happen when the first uncompleted `required` field is visible in the viewport when the form is submitted.
> Solution: The issue appears to be a bug on Chrome, as explained on [this post on Stack Overflow](https://stackoverflow.com/questions/69015407/html5-form-validation-message-doesnt-show-when-scroll-behaviour-is-set-to-smoo), caused by a combination of having `scroll-behavior: smooth` style set on the `html` element or `:root` pseudo selector, and the form being longer than the viewport window. (This is [also mentioned as a bug for Bootstrap 5](https://github.com/twbs/bootstrap/issues/33757) since `scroll-behavior:smooth` is set on `:root` in Bootstrap 5) Since the `scroll-behavior: smooth` is only affecting the PensionForm and is fine on the other pages, I created a short JavaScript function to change the `scroll-behavior` to `auto` for the Add Pension and Edit Pension pages:
```javascript
function changeScrollToAuto() {
    if(document.title === "Add Pension" || document.title === "Edit Pension") {
        document.documentElement.style.setProperty('scroll-behavior', 'auto')
    }
}
```
The HTML form validation error messages now display for non-completed `required` fields, however the scroll to the required field is not seamless. However the built in HTML validation and error messages is sufficient at this point in the project development. Later iterations of the project could include some client side validation of the form using JavaScript, to include a scroll to the field with the error, and/or to provide additonal error messages for the user.

- **Issue: Attribute Error on Edit Pension form file field if the data in the file field is not changed**
![Edit Pension form when file is not changed bug](docs/bugs/attribute-error-edit-pension-existing-file-bug.png)
The above error is raised when submitting the PensionForm on the EditPension view, when there is an existing file in the file field and it is not being changed, i.e. not clearing the existing file and not adding a new file.
> Solution: The error is happening in the `clean_file()` method on the `PensionForm`, because it is checking for the `name` of the file (to check if it doesn't end in .jpg or .png). However because the data in the field is not a new file but is an existing `CloudinaryResource object`, there is no `name` attribute. Added the check on the file name to a `try` block, and added an `except` block that passes on the `AttributeError` as this should only be raised if the file field contains an existing file i.e. a `CloudinaryResource object`. Since this file has already been checked when the file was initially added, and already exists on Cloudinary (the check is in place because Cloudinary gives a server error if the user tries to add a file like pdf, word document etc., so to give the user a proper error message) then in this case it seems reasonable to pass on the `AttributeError`.

- **Issue: Error when searching a foreign key in Django admin site**
![Admin searching with foreign key bug](docs/bugs/admin-search-foreign-key-bug.png)
The Django admin site gave the above error for the `Pension` model when trying to search the pensions records.
> Solution: This issue was caused by `'employment'` being included in the `search_fields` list. This is a `ForeignKey` field (linked to the `Job` model), so it needed to be referenced in the `search_fields` list using the name of the relevant field in the Job model, so in this case: `'employment__employer_name'`. I found the answer to this issue in [this Stack Overflow post](https://stackoverflow.com/questions/11754877/troubleshooting-related-field-has-invalid-lookup-icontains).

### Known Bugs
As noted in the [Test Cases - user stories](#test-cases---user-stories) section, a small bug was noticed with the Cancel button on the Add Job, Edit Job, Add Pension or Edit Pension forms. Originally the Cancel button was linked to bring the user back to the My Jobs page or My Pension page respectively. As the project progressed and there were more links to the Add/Edit forms from different locations (for easier user access), the Cancel button was amended to then bring the user back to the previous page, which would be in line with their expectations, instead of a hardcoded page. This functions correctly. However if the form is returned back to the user with errors (from the server side checking, before the details are commited to the database), then since the page with the form was refreshed, the user needs to press the Cancel button twice to get back to the previous page. The JavaScript function that handles this would need to be updated to check if the current page matches the previous window history, and if it does then go back one more. There is no scope to fix this in the current iteration of the project since it only came to light after completion. But it is a relatively small bug that will not affect all users and the level of errors completing the forms should be low since there are helptexts on the fields that might generate errors. 

### Supported Screens and Browsers
The project was developed using Chrome as the baseline browser.  

The website and the game functionality has been tested on my personal mobile device Galaxy A40 and a 15 inch MacBook Pro.

Using the [Chrome Dev Tools](https://developer.chrome.com/docs/devtools/) simulator, the website has been tested on the following screen sizes (px) equating to the phone models listed. *Note these have been tested on the simulator only and not the actual devices*:
- Moto G4, Galaxy S5:  360 x 640
- Pixel 2: 411 x 731
- Pixel 2 XL: 411 x 823
- iPhone 5/SE: 320 x 568
- iPhone 6/7/8: 375 x 667
- iPhone 6/7/8 Plus: 414 x 736
- iPhone X: 375 x 812
- iPad: 768 x 1024
- iPad Pro: 1024 x 1366
- Surface Duo: 540 x 720
