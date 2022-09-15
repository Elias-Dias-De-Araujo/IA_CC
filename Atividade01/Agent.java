public class Agent extends Perception {
    public void perceives(Enviroment e, String room) {
        this.setLocation(e.getAgentLocation());
        if (room.equals("A")) {
            this.setDirty(e.getIsDirtyA());
        } else {
            this.setDirty(e.getIsDirtyB());
        }
    }

    public Action act() {
        Action a = new Action();
        if (this.getIsDirty()) {
            a.setAction("Aspirar a sujeira");
            this.setDirty(false);
        } else {
            if (this.getLocation()) {
                a.setAction("Mover-se para direita");
            } else {
                a.setAction("Mover-se para esquerda");
            }
        }
        return a;
    }
}
