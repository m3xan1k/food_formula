import React, { Component, Fragment } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getDishes } from "../../actions/dishes";

export class Dishes extends Component {
  static propTypes = {
    dishes: PropTypes.array.isRequired,
  };

  componentDidMount() {
    this.props.getDishes();
  }

  render() {
    return (
      <Fragment>
        <h2>Dishes</h2>
            {this.props.dishes.map(dish => (
              <div className="card" key="{dish.id}">
              <h5 className="card-header">{dish.category.name}</h5>
              <div className="card-body">
              <h5 className="card-title">{dish.name}</h5>
              <p className="card-text">{ dish.description }</p>
              <a href="#" className="btn btn-secondary btn-block">Read more</a>
              {dish.tags.map(tag => (
                <a href="#" className="card-link">{tag.name}</a>
              ))}
              </div>
            </div>
            ))}
      </Fragment>
    );
  }
}

const mapStateToProps = state => ({
  dishes: state.dishes.dishes
});

export default connect(
  mapStateToProps,
  { getDishes }
)(Dishes);
