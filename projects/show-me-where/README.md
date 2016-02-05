Show Me Where project

A project showing me where things are.

"World Apart"

	About:
	Data files for school-level enrollment and student discipline (expulsion and suspension) in San Mateo County. Provenient from the California Department of Education. Data provides an important insight into the largely debated educational divide in Silicon Valey, in which thousands of low-income kids—most of whom have immigrant parents—are missing out on the early education they need to keep up with their affluent peers.


### Data set 1: Enrollment by School (2014-15) ###
Data for school-level enrollment by racial/ethnic designation, gender, and grade. Posted Apr-2015.

2. Basic Facts
	- Source: California Department of Education
	- Landing page: http://www.cde.ca.gov/ds/sd/sd/filesenr.asp
	- Direct URL: http://dq.cde.ca.gov/dataquest/dlfile/dlfile.aspx?cLevel=School&cYear=2014-15&cCat=Enrollment&cPage=filesenr.asp
	- Data format: 
		.txt (from download with information for all counties in California); 
		.csv (filtered with trifacta to show only San Mateo County)
	- Number of rows: 129355 (unfiltered)
	  				  2462 (filtered)

3. Description of data fields
	- CDS_CODE: text; This 14-digit code is the official, unique identification of a school within California. The first two digits identify the county, the next five digits identify the school district, and the last seven digits identify the school.

	- COUNTY: text; County name.

	- DISTRICT:	text; District name.

	- SCHOOL: text; School name.

	- ETHNIC: code; Racial/ethnic designation. This field is coded as follows:
		Code 0 = Not reported
		Code 1 = American Indian or Alaska Native, Not Hispanic
		Code 2 = Asian, Not Hispanic
		Code 3 = Pacific Islander, Not Hispanic
		Code 4 = Filipino, Not Hispanic
		Code 5 = Hispanic or Latino
		Code 6 = African American, not Hispanic
		Code 7 = White, not Hispanic
		Code 9 = Two or More Races, Not Hispanic

	- GENDER: text; Gender. This field is a coded as follows:
		M = Male
		F = Female

	- KDGN: Numeric; Students enrolled in kindergarten.

	- GR_1: Numeric; Students enrolled in grade one.

	- GR_2: Numeric; Students enrolled in grade two.

	- GR_3: Numeric; Students enrolled in grade three.

	- GR_4: Numeric; Students enrolled in grade four.

	- GR_5: Numeric; Students enrolled in grade five.

	- GR_6: Numeric; Students enrolled in grade six.

	- GR_7: Numeric; Students enrolled in grade seven.

	- GR_8: Numeric; Students enrolled in grade eight.

	- GR_9: Numeric; Students enrolled in grade nine.

	- GR_10: Numeric; Students enrolled in grade ten.

	- GR_11: Numeric; Students enrolled in grade eleven.

	- GR_12: Numeric; Students enrolled in grade twelve.

4. Data Wrangling:
	I have cleaned the data using Trifacta to extract Adult Education students, all California counties except for San Mateo, and ungraded enrollment programs.


	####################################################


### Data set 2: Expulsion and Suspension Data (2014-2015) ###
Data containing student expulsion and suspension data by ethnicity. The file contains the total suspensions and expulsions reported by each local educational agency. Posted Dec-2015.

2. Basic Facts
	- Source: California Department of Education
	- Landing page: http://www.cde.ca.gov/ds/sd/sd/filesesd.asp
	- Direct URL: http://dq.cde.ca.gov/dataquest/SuspExp/DownloadData.aspx?TheYear=2014-15
	- Data format: 
		.txt (from download with information for all counties in California); 
		.csv (filtered with trifacta to show only San Mateo County)
	- Number of rows: 69327 (unfiltered)
	  				  108 (filtered)

3. Description of data fields
	- AGGLEVEL: text; This field is a coded as follows:
		D=Local educational agency totals (includes districts and direct funded charter schools)
		O=County totals
		S=School totals
		T=State totals

	- CDS_CODE: text; This 14-digit code is the official unique identification of a school within California.  The first two digits identify the county, the next five digits identify the school district, and the last seven digits identify the school.

	- NAME: text; Name of the county, district, or school depending on the AGGLEVEL.

	- DISCIPLINE_TYPE: text; 
		E=Expulsion
		I=In-School Suspension
		O=Out-of-School Suspension

	- ETHNICITY: text; 
		0=Not Reported
		1=American Indian or Alaskan Native, not Hispanic
		2=Asian, not Hispanic
		3=Pacific Islander, not Hispanic
		4=Filipino, not Hispanic
		5=Hispanic or Latino
		6=African American, not Hispanic
		7=White, not Hispanic
		9=Two or more races, not Hispanic

	- WEAPONS: text; Number of suspensions or expulsions under the "Weapons Possession" Federal category.

	- DRUGS: text; Number of suspensions or expulsions under the "Illicit Drug Related" Federal category.

	- VIOLENCE_WITH_INJURY: text; Number of suspensions or expulsions under the "Violence with Injury" Federal category.

	- VIOLENCE_WITHOUT_INJURY: text; Number of suspensions or expulsions under the "Violence without Injury" Federal category.

	- OTHER_NOT_DEFIANCE: text; Number of suspensions or expulsions under the "Other" Federal category, not including those students disciplined for "Defiance."

	- OTHER_DEFIANCE_ONLY: text; Number of suspensions or expulsions under the "Other" Federal category for "Defiance" only.

	- TOTAL: text; Total number of suspensions or expulsions.

	- YEAR: text; Year of data.

	- DATE_CREATED: Number; Date of CALPADS submission deadline.

	- DATE_UPDATED: Number; The date of the most recent content addition or modification.

4. Data Wrangling:
	I have cleaned the data using Trifacta to extract all California counties except for San Mateo.
