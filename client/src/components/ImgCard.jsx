import { ImageListItem } from "@mui/material";

// can use for any gallery, but will both vert and horiz work or do I need separate V and H imgCards?

function ImgCard({ id, title, location, year, path}) {

    return(
        <ImageListItem key = { id }>
            <img
                src = { path }
                alt = { title }
            />
        </ImageListItem>
    );
}

export default ImgCard;
