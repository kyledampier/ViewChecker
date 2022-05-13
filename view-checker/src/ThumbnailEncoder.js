import React from "react";
import { Container, Grid } from "@mui/material/";
import TextField from "@mui/material/TextField";

const uploadStyle = {
    width: "90%",
    height: "40vh",
    borderRadius: "5px",
    padding: "0.5em",
    backgroundImage: "url(https://source.unsplash.com/random)",
    backgroundSize: "cover",
    backgroundPosition: "center",
}

function ThumbnailEncoder(props) {

    const [thumbnail, setThumbnail] = React.useState(null);

    return (
        <div>
            <input
                type="file"
                accepts="image/*"
                style={uploadStyle}
                background={thumbnail}
                onChange={(obj) => {
                    console.log(obj.target.files[0]);
                    setThumbnail(URL.createObjectURL(obj.target.files[0]));
                    props.onChange(URL.createObjectURL(obj.target.files[0]));
                }}
            />
        </div>
    );
}

export default ThumbnailEncoder;