import { legacy_createStore as createStore, applyMiddleware, compose } from 'redux';
import { composeWithDevTools } from '@redux-devtools/extension';
import {thunk} from 'redux-thunk'; // Import thunk as default export
import rootReducer from './reducers';

const initialState = {};

const middleware = [thunk];

const store = createStore(
    rootReducer,
    initialState,
    composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
