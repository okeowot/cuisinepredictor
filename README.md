# THIS IS PROJECT 2 AND MY NAME IS TOLULOPE OKEOWO. 
# THIS PROJECT IS RAN BY NAVIGATING TO THE CS5293SP23-PROJECT2 DIRECTORY. WHEN IN THAT DIRECTORY, YOU CAN RUN THE COMMAND "PIPENV RUN PYTHON PROJECT2" FOLLOWED BY THE N PARAMETER AND THE VARIOUS INGREDIENTS. THE CODE CAN BE INSTALLED BY GIT PULLING THE CODE FROM GITHUB AND THE PIPFILE CONTAINS ALL THE PACKAGES USED. 
# I DIDN'T USE ANY FUNCTION IN THIS PROGRAM. THE WAY THE PROGRAM WORKS IS IT HANDLES THE PARAMETERS THAT ARE SUPPOSED TO BE INSERTED BY THE USER WHICH ARE THE INGREDIENTS AND THE TOP N CUISINES THAT MATCH THOSE INGREDIENTS. ARGPARSER WAS USED TO HANDLE THAT PROCESS. 
# AFTER THAT WAS DONE, THE DATA IS LOADED INTO THE PROGRAM USING WITH OPEN WHICH WOULD ENABLE US TO READ THE CONTENTS OF THE FILE AND ASSIGN IT TO A VARIABLE. AFTER LOADED, A LIST WAS MADE THAT CONSISTED OF ALL THE INGREDIENTS FROM THE JSON FILE. ANOTHER STRING WAS MADE WHICH CONSISTED OF THE INGREDIENTS INPPUTTED BY THE USER. THE STRING WAS CONVERTED TO A LIST AND ADDED TO THE END OF THE LIST OF ALL THE INGREDIENTS. 
# A TF-IDF VECTORIZER WAS USED TO GET THE WEIGHTS OF EACH WORD IN THE CORPUS. I DIVIDED THE VALUES GOTTEN INTO 2 PARTS. ONE FOR JUST THE INGREDIENTS FROM JSON FILE AND THE SECOND WAS FOR THE INGRIDENTS INPUTTED BY THE USER. AFTER THIS WAS DONE, A COSINE SIMILARITY WAS PERFORMED BETWEEN BOTH VECTORS TO FIND THE SIMILARITY BETWEEN THEM. AFTER THE SIMILARITIES WAS FOUND, I THEN SORTED THE INDEXES OF THE SIMILARITES IN DECENDING ORDER WITH THE HIGHEST INDEX REPRESENTING A COSINE SIMILARITY SCORE FIRST. A VARIABLE SORTED_SIMILARITIES WAS THE ASSIGNED TO THESE SCORES. 
# THE VARIABLE SCORE_OF_MATCH WAS USED TO REPRESENT THE EXACT SIMILARITY SCORE FOR THE CUISINE MATCH WHICH WAS THE HIGHEST SCORE AND THE FIRST ELEMENT IN SORTED_SIMILARITIES. THE SCORE HAD TO BE CONVERTED TO A STRING BECAUSE IT WAS IN A NUMPY ARRAY TYPE. aFTER IT WAS CHANGED TO A STRING, SOME STRING SLICING HAD TO BE DONE TO TAKE OUT THE FIRST AND LAST ELEMENT BECAUSE IT WAS THE BRACKETS([]). THE EXACT CUISINE WAS GOTTEN BY ACCESSING THE FIRST ELEMENT IN THE SORTED_SIMILARITIES_INDEX WHICH PROVIDES THE INDEX OF THE HIGHEST COSINE SIMILARITY MATCH. THEN INDEXING THE DICTIONARY TO THE CUISINE GIVES THE EXACT MATCH. 
# SINCE I HAD THE SCORES IN SORTED IN SORTED_SIMILARITIES, I USED A FOR LOOP TO LOOP FROM 1 TO ARGS.N + 1 SO AS TO PRINT THE NEXT N CLOSE CUISINES. I ALSO HAD TO CONVERT THE VALUES GOTTEN INTO STRINGS AND SLICE OUT THE FIRST AND LAST ELEMENT BECAUSE THEY WERE BRACKETS([]). AFTER SLICING, I APPENDED THE SCORES INTO AN ARRAY TOP_N_SCORES.
# I MADE A DICTIONARY FOR HANDLING THE FORMAT OF HOW THE JSON FILE IS SUPPOSED TO LOOK. THEN FOR THE CLOSEST, I HAD ANOTER DICTIONARY THAT CONTAINED THE IDS AND SCORES.THE ID WAS GOTTEN FROM THE SORTED_SIMILARITIES_INDEX VARIABLE ALONG WITH THE ID PARAMETER WITH THE DATA VARIABLE. THE SCORES WERE GOTTEN BY ITERATING OVER THE TOP_N_SCORES VARIABLE FOR EACH NUMBER UNTIL --N WAS REACHED. 
# FOR MY TEST FILE, I USED TEST AGRUMENTS FOR THE INGREDIENTS WHICH WE WERE GIVEN(PAPRIKA, BANANA, RICE KRISPIES), THE --N AS 2 ALSO. I STORED THESE VARIABLES IN TEST_ARGS. AFTER THAT, I FOUND THE VALUES AND COMPARED THEM TO THE ONES I HAD MANUALLY PUT IN AS EXPECTED SOLUTION FROM RUNNING MY PROGRAM.  
https://user-images.githubusercontent.com/37723627/234436197-ea3b81a6-5152-4aa3-8dce-9a1e21d336ff.mov
