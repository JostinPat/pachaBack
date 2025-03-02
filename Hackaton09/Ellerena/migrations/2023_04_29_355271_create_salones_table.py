from orator.migrations import Migration


class CreateSalonesTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("salones") as table:
            table.increments("id")
            table.text("nombre")
            table.text("periodo")
            table.integer("alumno_id").unsigned()
            table.integer("profesor_id").unsigned()
            table.timestamps()

            table.foreign("alumno_id").references("id").on("salones").on_delete(
                "cascade"
            )
            table.foreign("profesor_id").references("id").on("salones").on_delete(
                "cascade"
            )

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("salones")