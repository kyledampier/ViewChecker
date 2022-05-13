import TextField from '@mui/material/TextField';
import LinearProgress from '@mui/material/LinearProgress';

function TextEncoder(props) {
    return (
        <div>
            <TextField
                label="Video Title"
                id="title-input"
                variant="outlined"
                fullWidth
                onPointerLeave={(obj) => {
                    console.log(obj.target.value);
                    props.onChange(obj.target.value);
                }}
            />
        </div>
    );
}

export default TextEncoder;