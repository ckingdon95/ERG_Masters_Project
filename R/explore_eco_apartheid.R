library(dplyr)
library(leaflet)
library(sf) # need to load this package for dplyr to work with the spatial dataframe

setwd("C:/Users/corak/Dropbox/ucb/spring2023/masters/R/")

data.dir = "../data/eco-apartheid/"

fp = file.path(data.dir, "final_eco_data_PCA_2021-02-01.RDS")

df = data.frame(readRDS(fp))

# view the polygon outlines
leaflet() %>%
    addTiles() %>%
    addPolygons(data = df$geometry)

# filter to just LA area
LA_df = df %>%
    filter(metro == "Los Angeles-Long Beach-Anaheim, CA")

# view the polygon outlines for LA
leaflet() %>%
    addTiles() %>%
    addPolygons(data = LA_df$geometry)

# Save LA data
LA_df %>%
    select(-geometry) %>%
    write.csv(file.path(data.dir, "LA_eco_data.csv"), row.names=FALSE)
