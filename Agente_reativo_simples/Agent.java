public class Agent {
    public Perception perceives(Enviroment env) {
        Perception p = new Perception();
        if(env.isAgentLocation()) {
            p.setDirty(env.isDirtyA());
            p.setLocation(env.isAgentLocation());
        }else {
            p.setDirty(env.isDirtyB());
            p.setLocation(env.isAgentLocation());
        }

        return p;
    }  

    public Action act(Perception p) {
        Action a = new Action();
        if(p.isDirty()){
            a.setName("aspirar");
        }else {
            if(p.isLocation()) {
                a.setName("direita");
            }else {
                a.setName("esquerda");
            }
        }
        return a;
    }
}
