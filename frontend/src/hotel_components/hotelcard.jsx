import './hotels.css'

import Card from 'react-bootstrap/Card';



function Hotelcard() {
 


  return (
    <Card style={{ width: '300px', border:'1px'}} >
      <img variant="top" src="" className='image' style={{objectFit:'cover', borderRadius:'5px'}}/>
      <Card.Body className='cards'>
        <Card.Title>name</Card.Title>
        <Card.Text>
         AGE: <br/>
         BREED:
        </Card.Text>
     
        <button className='button-primary'>book</button>
      
      </Card.Body>
    </Card>
  );
}

export default Hotelcard;