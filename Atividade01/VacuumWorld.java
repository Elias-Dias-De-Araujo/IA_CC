public class VacuumWorld {
    public static void main(String[] args) {
        Agent age = new Agent();
        Enviroment env = new Enviroment(true, false, true);
        int moves = 2;
        while (moves > 0) {
            if (env.getAgentLocation()) {
                age.perceives(env, "A");
                System.out.println(age.act().getAction());
                env.setDirtyA(false);
                System.out.println("Sala A limpa");
                System.out.println(age.act().getAction());
                env.setAgentLocation(false);
            } else {
                age.perceives(env, "B");
                System.out.println(age.act().getAction());
                env.setDirtyB(false);
                System.out.println("Sala B limpa");
                System.out.println(age.act().getAction());
                env.setAgentLocation(false);
            }

            moves--;
        }
        System.out.println("Todas as salas estão limpas");
    }
}