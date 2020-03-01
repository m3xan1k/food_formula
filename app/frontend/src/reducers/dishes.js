import { GET_DISHES } from "../actions/types.js";

const initialState = {
  dishes: []
};

export default function (state = initialState, action) {
  switch (action.type) {
    case GET_DISHES:
      return {
        ...state,
        dishes: action.payload
      };
    default:
      return state;
  }
}
