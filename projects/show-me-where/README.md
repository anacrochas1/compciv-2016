Show Me Where project

A project showing me where things are.

"World Apart"

### Data set: Enrollment by School (2014-15) ###

1. About
	Data files for school-level enrollment in San Mateo County, by racial/ethnic designation, gender, and grade. Provenient from the California Department of Education, upoloaded to its website on April, 2015. Data provides an important insight into the largely debated educational divide in Silicon Valey, in which thousands of low-income kids—most of whom have immigrant parents—are missing out on the early education they need to keep up with their affluent peers.

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
