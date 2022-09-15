public class VacuumWorld {
    public static void main(String[] args) {
        Agent ag = new Agent();
        Enviroment env = new Enviroment(true, true, false);
        int count = 10;
        while(count>0) {
            System.out.println("O agente está na sala " + (env.isAgentLocation() ? "A" : "B"));
            Action act = ag.act(ag.perceives(env));
            System.out.println(act.isName());
            env.update(act);
            count--;
        }
    }
}
