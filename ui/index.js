import exppress from 'express';
const app = exppress();
app.use(exppress.json());
app.use(exppress.static('front/dist'));
const port = process.env.PORT || 8080;

app.listen(port, ()=>{
    console.log(`Listening on port ${port}`);
});

app.get('/health_check',(req, res) => {
    res.status(200).send({ msg: "Frontend is working properly"});
});
