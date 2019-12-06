# images-for-location-type-downloader
Jupyter Notebooks I used to find a particular in an old photo by gathering all images of churches in the area in question. **May be useful and adapted to all kinds of similar problems.**

## My particular problem
The images below were taken by my grandfather on a trip to Italy with his family in 1973. I wanted to now the exact location, but googling for the church did not yield any results.

![Photo of their car in front of the church](the_church.png) ![Photo of the car from the other side](the_church_surroundings.png)

**How does this help to solve the problem?**
The `church_finder.ipynb` retrieves all buildings of type `church` in the relevant area from OpenStreetMaps and then downloads six images for each of them. I then simply looked through those images (after organising them differently using `rearrange_images.ipynv`) and looked for the church I saw in the original photo.

This may be adapted to all kinds of similar problems by changing the query to OpenStreetMaps to whatever one might be interested to find.
