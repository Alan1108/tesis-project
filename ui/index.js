import exppress from 'express';
import path from 'path'
const app = exppress();
const __dirname = path.resolve();
app.use(exppress.json());
app.use(exppress.static(path.join(__dirname, 'front/dist')));
const port = process.env.PORT || 8080;

app.listen(port, ()=>{
    console.log(`Listening on port ${port}`);
});

app.get('*', (req, res) => {
    res.sendFile(path.join(__dirname, 'front/dist/index.html'));
  });

app.get('/',(req, res) => {
    res.status(200).send({ msg: "Frontend is working properly"});
});
