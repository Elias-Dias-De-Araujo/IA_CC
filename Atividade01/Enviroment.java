public class Enviroment {
    private boolean isDirtyA;
    private boolean isDirtyB;
    private boolean agentLocation;
    
    public Enviroment(boolean isDirtyA, boolean isDirtyB, boolean agentLocation) {
        this.isDirtyA = isDirtyA;
        this.isDirtyB = isDirtyB;
        this.agentLocation = agentLocation;
    }

    public void update(Action action) {
        if(action.isName().equalsIgnoreCase("aspirar")) {
            if(agentLocation) {
                this.setDirtyA(false);
            }else {
                this.setDirtyB(false);
            }
        }else if(action.isName().equalsIgnoreCase("direita")) {
            if(agentLocation) {
                this.setAgentLocation(false);
            }
        }else if(action.isName().equalsIgnoreCase("esquerda")) {
            if(agentLocation == false) {
                this.setAgentLocation(true);
            }
        }
    }
    
    public boolean isDirtyA() {
        return isDirtyA;
    }

    public void setDirtyA(boolean isDirtyA) {
        this.isDirtyA = isDirtyA;
    }

    public boolean isDirtyB() {
        return isDirtyB;
    }

    public void setDirtyB(boolean isDirtyB) {
        this.isDirtyB = isDirtyB;
    }

    public boolean isAgentLocation() {
        return agentLocation;
    }

    public void setAgentLocation(boolean agentLocaltion) {
        this.agentLocation = agentLocaltion;
    }

    
}
