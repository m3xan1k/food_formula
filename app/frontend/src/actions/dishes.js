import axios from "axios";

import { GET_DISHES } from "./types";

// GET DISHES
export const getDishes = () => (dispatch) => {
  axios
    .get("/dishes/dish/")
    .then(res => {
      dispatch({
        type: GET_DISHES,
        payload: res.data
      });
    })
    .catch(err =>
      console.log(err)
    );
};
