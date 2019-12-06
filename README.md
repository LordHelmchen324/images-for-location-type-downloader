# images-for-location-type-downloader
Jupyter Notebooks I used to find a particular in an old photo by gathering all images of churches in the area in question. **May be useful and adapted to all kinds of similar problems.**

## My particular problem
The left photo below shows my grandparents' car in front of a church on a family trip to Lake Garda, Italy in 1973. I wanted to now the exact location, but googling for the church for days did not yield any results.

<p align="middle">
    <img src="the_church.png" width="300" />
    <img src="the_church_today.png" width="312" />
</p>

**Eureka!**

Using some Python skills, I retrieved all buildings of type `church` in the relevant area from OpenStreetMap and then downloaded six images for each of them from Google's image search (`church_finder.ipynb`). Then all it took was a little reorganisation of the dowloaded images (`rearrange_images.ipynb`), clicking through them, and ... voilà ... the photo's location was found. Above image to the right shows Chiesa di San Pietro in the village of Praso, Italy, photographed in 2015.

This solution may be adapted to all kinds of similar problems by changing the query to OpenStreetMap to whatever one might be interested to find.
