# web-analytics
Web traffic analytics built in flask and mongoengine

## SOME TIPS ON GIT

1. Always pull before start working
2. After making changes, use SourceTree to add the files and commit them with a meaningful message
3. Press push to upload the changes to the server
4. Use gitigore to ignore certain files, files like .pyc (generated from .py file), or any other generated files from the source file and some 

## TODO
1. Add a basic flask app
2. Create a few dummy routing: /about, /contact, /team
3. Create a routing for tracking /track-view
4. Create templates for each page
5. Add js codes to call the tracking url
6. Create mongoengine model to store data
7. Create an admin interface to view data, /dashboard

## FUTURE TODO
1. Capture visit duration of each page, using cookies or localstorage (needs research)
2. Capture visit duration of the whole site
3. Integrate geoip to get the country and city of the visitor
4. Create graphs in admin interface to view the data clearer
5. Add date filter in admin to view data of different date range

## CURRENT BEING DONE
1. Research on the impact of either using aggregation or running scheduled procedures. (by 3rd november)
2. Designing a database structure as performing aggregation in queries all the time with existing design may be costly. (by 3rd november)
3. Determine on when and how the scheduled task will be executed. Few Options to be discussed (by 4th november)
4. Research on capture visit duration of pages.

