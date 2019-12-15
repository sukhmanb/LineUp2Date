import React from 'react';
import axios from 'axios';


class Welcome extends React.Component {
  constructor(props) {
    super(props);
    this.state = {value: ''};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    this.setState({value: event.target.value});
  }

  handleSubmit(event) {
    // alert('A name was submitted: ' + this.state.value);
    event.preventDefault();
    console.log(this.state.value)
    // axios.post('http://localhost:5000/signup', {
    //   email: this.state.value
    // }).then(response => {
    //   console.log("VI HAR SENDT INN !!!:")
    // }).catch(err => console.log("Error"))

    axios.post('http://localhost:5000/signup',{'email':this.state.value})
    .then(response => {
      console.log("VI HAR SENDT INN !!!:")
      // this.setState({ trumfdata: response.data })
    })
    .catch(err => console.log("Error", err))
  }

  render() {
    return (
      <div>
      <h1>Welcome to LineUp2Date</h1>
      <form method="get"onSubmit={this.handleSubmit}>
        <label>
          Email:
          <input type="email" value={this.state.value} onChange={this.handleChange} />
        </label>
        <br></br>
        <input type="submit" value="Submit" />
      </form>
      </div>
    );
  }
}

export default Welcome;
